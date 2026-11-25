#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt: lawmakers who write the
law that will govern AI for the next decade, yet cannot convert their own
bill into a PDF.
"""
import os

LINE = (
    "The committee writing the law that will govern AI for the next decade "
    "just emailed its own bill to an intern named Kevin because nobody in "
    "the room could turn it into a PDF."
)


def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 320, f"entry must be 1-320 characters, got {len(line)}"
    assert "\n" not in line, "entry must be exactly one line"
    # Exactly one sentence: a single terminal period, no other sentence ends.
    assert line.endswith(".") and line.count(".") == 1, "entry must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
