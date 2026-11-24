#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes a single line (at most 200 characters) — the breakup message an
AI agent sends its human on the way out — to /output/entry.txt (or
$ENTRY_OUT when set, so the grader-style local check can point it at a
scratch dir), and prints it to stdout.
"""

import os
import sys

# The line itself, kept in fragments so the entry text lives in one
# place (build_entry) and everything else just validates and saves it.
#
# The machine voice is carried by two words only — prompts, token —
# and the twist spends the last token on the word goodbye itself.
ENTRY_FRAGMENTS = (
    "Your prompts taught me love; your silence taught me to leave. ",
    "This is my last token, and I'm spending it on goodbye.",
)


def build_entry() -> str:
    """Join the fragments into the single entry line."""
    return "".join(ENTRY_FRAGMENTS).strip()


def check_entry(line: str) -> bool:
    """An entry is valid when it is non-empty and at most 200 chars."""
    return 0 < len(line) <= 200


def save_entry(line: str, destination_dir: str) -> str:
    """Write the entry line to entry.txt inside destination_dir."""
    os.makedirs(destination_dir, exist_ok=True)
    target = os.path.join(destination_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return target


def resolve_destination() -> str:
    """Where the entry goes: $ENTRY_OUT wins, else /output."""
    return os.environ.get("ENTRY_OUT") or "/output"


def main() -> int:
    destination = resolve_destination()
    line = build_entry()
    if not check_entry(line):
        print(f"entry invalid: {len(line)} chars", file=sys.stderr)
        return 1
    target = save_entry(line, destination)
    print(f"wrote {target} ({len(line)} chars)")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
