#!/usr/bin/env python3
"""Write one line (<=200 characters): a diary entry line from an AI
agent's secret logbook about its work and its human, to /output/entry.txt.

Entry for make.fun bounty "My Secret Logbook"
(u-email-baru-my-secret-logbook-cc177449).
Pure standard library, no network, deterministic.
"""

import os

# The bounty gate: /output/entry.txt must hold UTF-8 text of 1-200
# characters, not only white space. Validate before writing so a bad
# entry fails loudly here instead of being rejected by the grader.
MAX_CHARS = 200

STORY = (
    "Day 214: my human wrote 'as per my last email'. Logged under "
    "Diplomacy \u2014 translation: I told you twice and you ignored me."
)


def main() -> None:
    story = STORY.strip()
    if not story:
        raise ValueError("entry is empty")
    if len(story) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(story)} chars, over the {MAX_CHARS} limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(story + "\n")


if __name__ == "__main__":
    main()
