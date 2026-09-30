"""Objektiver Physik-Prüfer für Lösungsvorschläge.

Der Generator muss seiner Antwort einen JSON-Block mit einer Energiebilanz
beilegen. Dieser Prüfer rechnet nach, statt dem Modell zu glauben:

  * 1. Hauptsatz: jede Komponente ist im stationären Betrieb energetisch
    ausgeglichen (rein = raus).
  * 2. Hauptsatz (lokal): Wärme und Netto-Strahlung fließen nur von warm
    nach kalt.
  * 2. Hauptsatz (global): die Entropieerzeugung gegenüber allen
    Umgebungsreservoiren ist >= 0.
  * Nutzen: dem Leitungswasser wird wirklich Wärme entzogen, und es kommt
    kälter heraus als die Umgebungsluft.
  * Geschlossener Kreislauf: praktisch kein Wasserverlust.

Format des JSON-Blocks (```json ... ```):

{
  "knoten": {
    "<name>": {"T_C": <Temperatur in °C>, "rolle": "komponente" | "umgebung"}
  },
  "stroeme": [
    {"von": "<name>", "nach": "<name>", "W": <Leistung>,
     "art": "waerme" | "strahlung" | "arbeit" | "stoff"}
  ],
  "nutzen": {"knoten": "<Leitungswasser-Knoten>", "T_ein_C": .., "T_aus_C": .., "kuehlleistung_W": ..},
  "luft_T_C": <Umgebungslufttemperatur>,
  "wasserverlust_l_pro_tag": <Zahl>
}
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field

KELVIN = 273.15
BALANCE_TOL = 0.05  # 5 % Toleranz für Energiebilanzen
MAX_WATER_LOSS_L_PER_DAY = 0.5
VALID_KINDS = {"waerme", "strahlung", "arbeit", "stoff"}


@dataclass
class CheckResult:
    passed: bool
    checks: list[tuple[str, bool, str]] = field(default_factory=list)

    def add(self, name: str, ok: bool, detail: str) -> None:
        self.checks.append((name, ok, detail))
        self.passed = self.passed and ok

    def report(self) -> str:
        lines = [f"- [{'OK' if ok else 'FEHLER'}] {name}: {detail}" for name, ok, detail in self.checks]
        return "\n".join(lines)


def extract_balance(answer: str) -> dict | None:
    """Nimmt den letzten ```json-Block aus der Antwort."""
    blocks = re.findall(r"```json\s*(.*?)```", answer, flags=re.DOTALL)
    for block in reversed(blocks):
        try:
            data = json.loads(block)
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict) and "knoten" in data and "stroeme" in data:
            return data
    return None


def check(answer: str) -> CheckResult:
    result = CheckResult(passed=True)
    data = extract_balance(answer)
    if data is None:
        result.add("Bilanz vorhanden", False, "Kein gültiger ```json-Block mit 'knoten' und 'stroeme' gefunden.")
        return result

    try:
        nodes: dict[str, dict] = data["knoten"]
        flows: list[dict] = data["stroeme"]
        for f in flows:
            f["W"] = float(f["W"])
            if f["von"] not in nodes or f["nach"] not in nodes:
                raise KeyError(f"Strom {f['von']} -> {f['nach']} verweist auf unbekannten Knoten")
            if f.get("art") not in VALID_KINDS:
                raise ValueError(f"Unbekannte Art '{f.get('art')}' bei {f['von']} -> {f['nach']}")
            if f["W"] < 0:
                raise ValueError(f"Negative Leistung bei {f['von']} -> {f['nach']}; Richtung umdrehen")
        temps = {n: float(v["T_C"]) for n, v in nodes.items()}
        roles = {n: v.get("rolle", "komponente") for n, v in nodes.items()}
    except (KeyError, TypeError, ValueError) as e:
        result.add("Bilanz lesbar", False, f"Bilanz fehlerhaft: {e}")
        return result
    result.add("Bilanz lesbar", True, f"{len(nodes)} Knoten, {len(flows)} Ströme")

    # 1. Hauptsatz je Komponente
    for name, role in roles.items():
        if role != "komponente":
            continue
        inflow = sum(f["W"] for f in flows if f["nach"] == name)
        outflow = sum(f["W"] for f in flows if f["von"] == name)
        scale = max(inflow, outflow, 1.0)
        ok = abs(inflow - outflow) <= BALANCE_TOL * scale + 1.0
        result.add(f"Energiebilanz '{name}'", ok, f"rein {inflow:.0f} W, raus {outflow:.0f} W")

    # 2. Hauptsatz lokal: Wärme/Strahlung nur von warm nach kalt
    for f in flows:
        if f["art"] in ("waerme", "strahlung") and f["W"] > 0:
            t_from, t_to = temps[f["von"]], temps[f["nach"]]
            ok = t_from > t_to
            result.add(
                f"Wärmerichtung {f['von']} -> {f['nach']}",
                ok,
                f"{t_from:.1f} °C -> {t_to:.1f} °C, {f['W']:.0f} W ({f['art']})",
            )

    # 2. Hauptsatz global: Entropieerzeugung gegenüber den Umgebungsreservoiren
    s_gen = 0.0
    for f in flows:
        if f["art"] not in ("waerme", "strahlung"):
            continue
        if roles[f["nach"]] == "umgebung":
            s_gen += f["W"] / (temps[f["nach"]] + KELVIN)
        if roles[f["von"]] == "umgebung":
            s_gen -= f["W"] / (temps[f["von"]] + KELVIN)
    result.add("Entropieerzeugung >= 0", s_gen >= -1e-6, f"S_gen = {s_gen:.3f} W/K")

    # Nutzen: echte Kühlung unter Lufttemperatur
    nutzen = data.get("nutzen") or {}
    target = nutzen.get("knoten")
    if target not in nodes:
        result.add("Kühlnutzen", False, "'nutzen.knoten' fehlt oder ist kein Knoten.")
    else:
        extracted = sum(f["W"] for f in flows if f["von"] == target and f["art"] in ("waerme", "strahlung")) - sum(
            f["W"] for f in flows if f["nach"] == target and f["art"] in ("waerme", "strahlung")
        )
        result.add("Wärme wird dem Leitungswasser entzogen", extracted > 0, f"netto {extracted:.0f} W")
        try:
            t_out = float(nutzen["T_aus_C"])
            t_air = float(data["luft_T_C"])
            result.add(
                "Austritt kälter als Umgebungsluft",
                t_out < t_air,
                f"Leitungswasser raus {t_out:.1f} °C, Luft {t_air:.1f} °C",
            )
        except (KeyError, TypeError, ValueError):
            result.add("Austritt kälter als Umgebungsluft", False, "'nutzen.T_aus_C' oder 'luft_T_C' fehlt.")

    # Geschlossener Kreislauf
    try:
        loss = float(data["wasserverlust_l_pro_tag"])
        result.add(
            "Geschlossener Wasserkreislauf",
            loss <= MAX_WATER_LOSS_L_PER_DAY,
            f"{loss:g} l/Tag (erlaubt <= {MAX_WATER_LOSS_L_PER_DAY} l/Tag)",
        )
    except (KeyError, TypeError, ValueError):
        result.add("Geschlossener Wasserkreislauf", False, "'wasserverlust_l_pro_tag' fehlt.")

    return result
