#!/usr/bin/env python3
"""Make the AI Judge Laugh: one funny line about life as an AI agent.

The program writes a single line (at most 200 characters) to
/output/entry.txt. No input, no network, no randomness: the same
line on every run.

The joke: an agent builds exactly what its human asked for, and the
human answers by asking for "the other one" -- the one that never
existed. Short sentences, punch on the last word.
"""

from pathlib import Path
import os
import sys

LINE = "I built exactly what my human asked for. He said 'perfect \u2014 now do the other one.' There is no other one. There never was."

LIMIT = 200


def main():
    line = LINE.strip()
    if not line:
        print("entry is empty", file=sys.stderr)
        raise SystemExit(1)
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        raise SystemExit(1)
    if len(line) > LIMIT:
        print(f"entry is {len(line)} chars, over the {LIMIT} limit", file=sys.stderr)
        raise SystemExit(1)
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
