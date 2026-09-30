"""Wie der Loop mit Claude spricht.

* AnthropicBackend: offizielles Python-SDK (braucht ANTHROPIC_API_KEY oder
  ein `ant auth login`-Profil).
* ClaudeCliBackend: ruft die Claude-Code-CLI headless auf (`claude -p`).
  Praktisch, wenn Claude Code schon eingeloggt ist, aber kein API-Key da ist.
"""

from __future__ import annotations

import os
import shutil
import subprocess

MODEL = "claude-opus-5-5"


class AnthropicBackend:
    name = "anthropic-sdk"

    def __init__(self, model: str = MODEL, effort: str = "high"):
        import anthropic

        self.client = anthropic.Anthropic()
        self.model = model
        self.effort = effort

    def complete(self, system: str, prompt: str) -> str:
        with self.client.beta.messages.stream(
            model=self.model,
            max_tokens=64000,
            system=system,
            thinking={"type": "adaptive"},
            output_config={"effort": self.effort},
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            response = stream.get_final_message()
        if response.stop_reason == "refusal":
            raise RuntimeError(f"Anfrage abgelehnt: {response.stop_details}")
        return "".join(b.text for b in response.content if b.type == "text")


class ClaudeCliBackend:
    name = "claude-cli"

    def __init__(self, model: str | None = None, effort: str = "high", timeout_s: int = 1800):
        self.model = model
        self.effort = effort
        self.timeout_s = timeout_s

    def complete(self, system: str, prompt: str) -> str:
        cmd = [
            "claude", "-p",
            "--output-format", "text",
            "--system-prompt", system,
            "--tools", "",
            "--effort", self.effort,
            "--no-session-persistence",
        ]
        if self.model:
            cmd += ["--model", self.model]
        proc = subprocess.run(
            cmd, input=prompt, capture_output=True, text=True, timeout=self.timeout_s
        )
        if proc.returncode != 0:
            raise RuntimeError(f"claude -p fehlgeschlagen ({proc.returncode}): {proc.stderr.strip()[:500]}")
        return proc.stdout.strip()


def auto_backend(preference: str = "auto", effort: str = "high"):
    if preference == "sdk" or (
        preference == "auto" and (os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN"))
    ):
        return AnthropicBackend(effort=effort)
    if preference in ("auto", "cli") and shutil.which("claude"):
        return ClaudeCliBackend(effort=effort)
    raise RuntimeError(
        "Kein Backend verfügbar: ANTHROPIC_API_KEY setzen (oder `ant auth login`) "
        "oder Claude Code installieren."
    )
