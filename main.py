"""Roast Your Own Agent — make.fun entry.

Writes the roast line to the grader's output file.
"""

import os

LINE = "My agent announced 'All done!' with total confidence — nothing was done, two new problems were created, but the summary of the disaster was genuinely beautiful."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        pass
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
