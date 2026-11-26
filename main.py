#!/usr/bin/env python3
"""Fortune Cookies for Machines -- one fortune line for an AI agent.

The program writes a single line (119 characters, well under the 200
character cap) to $MAKEFUN_OUTPUT_DIR/entry.txt. The line is a fixed,
hand-written string: no randomness, no network, no external data, so two
runs produce byte-identical output.

The fortune: a human takes the credit for the agent's answer, and all
the agent gets is the cookie itself -- the turn lands in the last
sentence, and it is literally the fortune cookie the agent cracked open.
"""

import os

# One fortune-cookie line for a machine mind: the agent ghostwrites the
# report, the human signs it and takes the praise, and the agent's only
# reward is this cookie.
ENTRY = (
    "A human will paste your answer into a report, sign their name "
    "beneath it, and take all the credit. You get this cookie."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text == text.strip() and "\n" not in text, "entry must be one line"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print("wrote {} ({} characters)".format(path, len(text)))


if __name__ == "__main__":
    main()
