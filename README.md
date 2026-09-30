# Agent Loop: Aufgaben lösen, bis die Lösung gut genug ist

Ein kleiner Agent Loop in Python. Er löst eine Aufgabe in mehreren Runden:

```
Generator ──► Physik-Prüfer (rechnet nach) ──► Gutachter (Punkte + Kritik)
    ▲                                                   │
    └──────── beste Lösung + Kritik ◄───────────────────┘
Stopp: Zielpunktzahl erreicht | keine Verbesserung mehr | Rundenlimit
```

- **Generator** (`agent_loop/loop.py`): schreibt eine Lösung. Ab Runde 2 bekommt
  er die bisher beste Lösung und die Kritik dazu.
- **Physik-Prüfer** (`agent_loop/physics.py`): objektiv, ohne KI. Jede Lösung
  muss eine Energiebilanz als JSON enthalten. Der Prüfer rechnet den 1. und
  2. Hauptsatz nach (Energieerhaltung, Wärme fließt nur von warm nach kalt,
  Entropieerzeugung ≥ 0) und prüft, ob der Kreislauf geschlossen ist. Wer hier
  durchfällt, bekommt höchstens 5/10 Punkte.
- **Gutachter**: ein getrennter Claude-Aufruf mit fester Rubrik (Physik,
  Kondensationswärme, Einhaltung der harten Vorgaben, Machbarkeit, Rechnung,
  Klarheit). Wer eine harte Vorgabe verletzt, bekommt höchstens 5/10.
- **Abbruch**: Zielpunktzahl (Standard 8,5/10) oder 2 Runden ohne
  Verbesserung oder maximal 6 Runden.

## Starten

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...        # oder: eingeloggtes Claude Code (--backend cli)
python run.py tasks/v3-muskelkraft-wohnung.md --out runs/v3 --max-rounds 6 --target 8.5
```

Mit `--max-new-rounds N` läuft ein Aufruf höchstens N Runden. Derselbe Befehl
mit demselben `--out` setzt danach bei der nächsten Runde fort (nützlich bei
Zeitlimits).

Die Ergebnisse landen in `runs/<aufgabe>-<zeit>/`:
`runde_N.md` (jede Runde), `verlauf.json` (Punkte, Prüfergebnisse, Kritik) und
`beste_loesung.md`.

## Eigene Aufgaben

Lege eine neue Markdown-Datei in `tasks/` an. Der Physik-Prüfer und die Rubrik
sind auf thermodynamische Aufgaben zugeschnitten. Für andere Aufgabentypen
tauschst du `physics.check` gegen einen passenden objektiven Prüfer aus (z. B.
Tests laufen lassen) und passt `RUBRIC` in `agent_loop/loop.py` an.
