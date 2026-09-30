"""Der eigentliche Agent Loop: erzeugen -> prüfen -> bewerten -> verbessern.

Pro Runde:
  1. Generator schreibt eine (verbesserte) Lösung.
  2. physics.check() rechnet die Energiebilanz objektiv nach.
  3. Ein getrennter Bewerter vergibt Punkte nach einer festen Rubrik.
  4. Beste Lösung merken; stoppen bei Zielpunktzahl, Plateau oder Rundenlimit.
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass
from pathlib import Path

from . import physics

GENERATOR_SYSTEM = """Du bist ein erfahrener Ingenieur für Thermodynamik und Kältetechnik.
Du entwirfst reale, baubare Anlagen und rechnest ehrlich. Du erfindest keine
Physik: Energie bleibt erhalten, Wärme fließt von selbst nur von warm nach
kalt, und jede Kühlung unter Umgebungstemperatur braucht eine kältere Senke
oder einen Antrieb (Arbeit oder Wärme hoher Temperatur). Antworte auf Deutsch,
verständlich für einen interessierten Laien, aber mit Zahlen."""

JUDGE_SYSTEM = """Du bist ein strenger, unabhängiger Gutachter für Thermodynamik und
Anlagenbau. Du hast die Lösung NICHT geschrieben. Suche aktiv nach Fehlern,
unrealistischen Annahmen und geschönten Zahlen. Antworte ausschließlich mit
einem JSON-Objekt, ohne Text davor oder danach."""

RUBRIC = {
    "physik": ("Physikalisch korrekt, keine verbotenen Wärmeflüsse, realistische Wirkungsgrade/COP", 0.25),
    "kondensationswaerme": ("Löst das Kernproblem der Aufgabe: wohin geht die Wärme (Wärmesenke, z. B. Kondensationswärme), und warum funktioniert das", 0.20),
    "vorgaben": ("Hält ALLE harten Vorgaben der Aufgabe ein (z. B. Arbeitsmittel, Strom, Größe); jede Verletzung ergibt höchstens 3 Punkte", 0.15),
    "machbarkeit": ("Baubar mit realen Materialien, Maße, Flächen, grobe Kosten, Wartung", 0.15),
    "quantifizierung": ("Nachvollziehbare Rechnung: Kühlleistung, Temperaturen, Flächen, Tag/Nacht", 0.15),
    "klarheit": ("Verständlich erklärt, ehrlich zu Grenzen und Risiken", 0.10),
}
# Unterhalb dieser Punktzahl bei "vorgaben" gilt die Lösung als Regelverstoß.
MIN_VORGABEN = 6.0

OUTPUT_FORMAT = """
## Ausgabeformat
1. Lösung als Markdown (Prinzip, Aufbau mit Skizze in ASCII, Rechnung, Grenzen).
2. Ganz am Ende GENAU EIN ```json-Block mit der Energiebilanz im stationären
   Betrieb (Auslegungsfall Tag). Format:

```json
{
  "knoten": {
    "<name>": {"T_C": <°C>, "rolle": "komponente" | "umgebung"}
  },
  "stroeme": [
    {"von": "<name>", "nach": "<name>", "W": <Leistung, positiv>, "art": "waerme" | "strahlung" | "arbeit" | "stoff"}
  ],
  "nutzen": {"knoten": "<Nutz-Knoten, z. B. Leitungswasser oder Wohnung>", "T_ein_C": <°C>, "T_aus_C": <°C>, "kuehlleistung_W": <W>},
  "luft_T_C": <°C>,
  "wasserverlust_l_pro_tag": <Liter>
}
```
Regeln für die Bilanz: "umgebung" sind unendlich große Reservoire (Luft,
Himmel, Sonne, Erdreich, Leitungswasser, Wohnung). "komponente" sind deine Bauteile;
für jede muss rein = raus gelten. "waerme" und "strahlung" müssen von warm nach
kalt zeigen (Netto-Strahlung). Latente Wärme, die mit Dampf/Kondensat zwischen
Bauteilen wandert, ist "stoff". Die Bilanz wird automatisch nachgerechnet.
"""


@dataclass
class Round:
    number: int
    answer: str
    physics: physics.CheckResult
    judge: dict
    score: float

    @property
    def rank(self) -> tuple[float, float]:
        # Bei gleich gedeckelten Punktzahlen entscheidet die ungedeckelte.
        return (round(self.score, 2), raw_score(self.judge))


def _extract_json(text: str) -> dict:
    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        raise ValueError("Bewerter hat kein JSON geliefert")
    return json.loads(match.group(0))


def judge(backend, task: str, answer: str, physics_report: str) -> dict:
    criteria = "\n".join(f'- "{k}": {desc} (Gewicht {w:.0%})' for k, (desc, w) in RUBRIC.items())
    prompt = f"""# Aufgabe
{task}

# Zu bewertende Lösung
{answer}

# Ergebnis des automatischen Physik-Prüfers
{physics_report}

# Bewertung
Vergib für jedes Kriterium 0-10 Punkte:
{criteria}

Antworte als JSON:
{{"punkte": {{{", ".join(f'"{k}": n' for k in RUBRIC)}}},
  "schwaechen": ["konkrete Schwäche + wie man sie behebt", ...],
  "staerken": ["...", ...]}}"""
    for attempt in range(2):
        raw = backend.complete(JUDGE_SYSTEM, prompt)
        try:
            data = _extract_json(raw)
            data["punkte"] = {k: float(data["punkte"][k]) for k in RUBRIC}
            return data
        except (ValueError, KeyError, TypeError):
            if attempt == 1:
                raise
    raise AssertionError("unreachable")


def raw_score(judgement: dict) -> float:
    return sum(judgement["punkte"][k] * w for k, (_, w) in RUBRIC.items())


def weighted_score(judgement: dict, physics_result: physics.CheckResult) -> float:
    score = raw_score(judgement)
    # Wer die Physik-Prüfung nicht besteht oder Vorgaben verletzt, kann nicht "gut genug" sein.
    if not physics_result.passed or judgement["punkte"]["vorgaben"] < MIN_VORGABEN:
        return min(score, 5.0)
    return score


def generate(backend, task: str, best: Round | None) -> str:
    if best is None:
        prompt = f"# Aufgabe\n{task}\n{OUTPUT_FORMAT}"
    else:
        weaknesses = "\n".join(f"- {s}" for s in best.judge.get("schwaechen", []))
        prompt = f"""# Aufgabe
{task}

# Bisher beste Lösung (Runde {best.number}, Punktzahl {best.score:.2f}/10)
{best.answer}

# Automatischer Physik-Prüfer
{best.physics.report()}

# Kritik des Gutachters
{weaknesses}

# Auftrag
Schreibe eine vollständig überarbeitete, bessere Lösung. Behebe jeden Fehler
des Physik-Prüfers und jede Schwäche des Gutachters. Wenn ein Ansatz
grundsätzlich nicht funktioniert, wechsle den Ansatz, statt ihn zu schönen.
Gib die komplette Lösung aus, nicht nur die Änderungen.
{OUTPUT_FORMAT}"""
    return backend.complete(GENERATOR_SYSTEM, prompt)


def _resume(out_dir: Path, log) -> tuple[Round | None, int, list]:
    """Lädt einen unterbrochenen Lauf aus verlauf.json und runde_N.md."""
    path = out_dir / "verlauf.json"
    if not path.exists():
        return None, 0, []
    history = json.loads(path.read_text(encoding="utf-8"))
    best: Round | None = None
    stale = 0
    for h in history:
        judgement = {"punkte": h["punkte"], "schwaechen": h["schwaechen"], "staerken": h["staerken"]}
        candidate = (round(h["score"], 2), raw_score(judgement))
        if best is None or candidate > best.rank:
            answer = (out_dir / f"runde_{h['runde']}.md").read_text(encoding="utf-8")
            best, stale = Round(h["runde"], answer, physics.check(answer), judgement, h["score"]), 0
        else:
            stale += 1
    if best is not None:
        log(f"Setze fort nach Runde {len(history)} (beste bisher: Runde {best.number}, {best.score:.2f}/10).")
    return best, stale, history


def run(
    backend,
    task: str,
    out_dir: Path,
    max_rounds: int = 6,
    target: float = 8.5,
    patience: int = 2,
    max_new_rounds: int | None = None,
    log=print,
) -> Round:
    out_dir.mkdir(parents=True, exist_ok=True)
    best, stale, history = _resume(out_dir, log)
    first = len(history) + 1
    last = max_rounds if max_new_rounds is None else min(max_rounds, first + max_new_rounds - 1)

    if best is not None and (best.score >= target and best.physics.passed or stale >= patience):
        log("Lauf ist bereits abgeschlossen.")
        last = first - 1  # keine neuen Runden

    for n in range(first, last + 1):
        t0 = time.time()
        log(f"\n=== Runde {n}/{max_rounds}: Generator schreibt ...")
        answer = generate(backend, task, best)
        phys = physics.check(answer)
        log(f"Physik-Prüfer: {'bestanden' if phys.passed else 'NICHT bestanden'}\n{phys.report()}")
        log("Gutachter bewertet ...")
        judgement = judge(backend, task, answer, phys.report())
        score = weighted_score(judgement, phys)
        rnd = Round(n, answer, phys, judgement, score)
        log(f"Punkte: {judgement['punkte']} -> gewichtet {score:.2f}/10 ({time.time() - t0:.0f}s)")

        (out_dir / f"runde_{n}.md").write_text(answer, encoding="utf-8")
        history.append(
            {
                "runde": n,
                "score": round(score, 2),
                "punkte": judgement["punkte"],
                "physik_bestanden": phys.passed,
                "physik": [{"check": c, "ok": ok, "detail": d} for c, ok, d in phys.checks],
                "schwaechen": judgement.get("schwaechen", []),
                "staerken": judgement.get("staerken", []),
            }
        )
        (out_dir / "verlauf.json").write_text(json.dumps(history, indent=2, ensure_ascii=False), encoding="utf-8")

        if best is None or rnd.rank > best.rank:
            best, stale = rnd, 0
        else:
            stale += 1

        if best.score >= target and best.physics.passed:
            log(f"Ziel erreicht ({best.score:.2f} >= {target}).")
            break
        if stale >= patience:
            log(f"Keine Verbesserung seit {patience} Runden - Stopp.")
            break
    else:
        if last >= max_rounds:
            log("Rundenlimit erreicht.")
        elif last >= first:
            log(f"Pause nach Runde {last} - mit denselben Argumenten erneut starten, um fortzusetzen.")

    if best is None:
        raise RuntimeError("Keine Runde gelaufen.")
    (out_dir / "beste_loesung.md").write_text(best.answer, encoding="utf-8")
    log(f"\nBeste Lösung: Runde {best.number}, {best.score:.2f}/10 -> {out_dir / 'beste_loesung.md'}")
    return best
