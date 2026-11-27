"""Entry for 'One Emoji, One Dream Vacation' (make.fun).

Writes exactly one emoji, 1 to 8 characters, to /output/entry.txt: the
entrant's dream vacation, wordless, like a postcard.
"""

import os

ENTRY = "🏝️"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
