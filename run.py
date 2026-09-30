"""Startet den Agent Loop für eine Aufgabe.

Beispiel:
    python run.py tasks/verdunstungskuehlung.md --max-rounds 6 --target 8.5
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

from agent_loop import backends, loop


def main() -> int:
    parser = argparse.ArgumentParser(description="Agent Loop: lösen, prüfen, verbessern")
    parser.add_argument("task", type=Path, help="Markdown-Datei mit der Aufgabe")
    parser.add_argument("--max-rounds", type=int, default=6)
    parser.add_argument("--target", type=float, default=8.5, help="Zielpunktzahl 0-10")
    parser.add_argument("--patience", type=int, default=2, help="Runden ohne Verbesserung bis Stopp")
    parser.add_argument("--backend", choices=["auto", "sdk", "cli"], default="auto")
    parser.add_argument("--effort", default="high", choices=["low", "medium", "high", "xhigh", "max"])
    parser.add_argument("--out", type=Path, default=None, help="Ausgabeordner (Standard: runs/<aufgabe>-<zeit>)")
    args = parser.parse_args()

    task = args.task.read_text(encoding="utf-8")
    out = args.out or Path("runs") / f"{args.task.stem}-{datetime.now():%Y%m%d-%H%M%S}"
    backend = backends.auto_backend(args.backend, effort=args.effort)
    print(f"Backend: {backend.name} | Ausgabe: {out}", flush=True)

    best = loop.run(
        backend, task, out,
        max_rounds=args.max_rounds, target=args.target, patience=args.patience,
        log=lambda msg: print(msg, flush=True),
    )
    return 0 if best.physics.passed else 1


if __name__ == "__main__":
    sys.exit(main())
