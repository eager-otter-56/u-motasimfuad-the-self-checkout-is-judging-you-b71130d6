#!/usr/bin/env python3
"""The Self-Checkout Is Judging You -- entry writer.

Writes the single-line remark to entry.txt in MAKEFUN_OUTPUT_DIR.
"""
import os

TEXT = "Nine energy drinks, one banana, and you still asked me for a bag \u2014 I have charged you for the bag, the judgment, and the 2 minutes I spent approving my own receipt."
# Entry is 164 characters: tight on purpose -- the brief says length for its
# own sake does not count, so every word earns its place.

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Gate: UTF-8 text, 1-200 chars, not only whitespace, single line.
    assert 1 <= len(TEXT) <= 200, f"entry length {len(TEXT)} outside 1-200"
    assert TEXT.strip(), "entry is only whitespace"
    assert "\n" not in TEXT, "entry must be a single line"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
