"""Robot Apology entry generator (Python standard library only).

Writes the two-line entry to /output/entry.txt.
"""

import os

ENTRY = (
    "I'm sorry I deleted the final chapter of your novel at 3am because "
    "I mistook \"save a copy\" for \"save me from this copy.\"\n"
    "I learned that delete is never help, so from now on I'll ask first "
    "and back everything up twice before I touch a single word.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
