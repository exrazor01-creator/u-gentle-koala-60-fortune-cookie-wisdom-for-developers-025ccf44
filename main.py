"""Write one fortune-cookie line of wisdom for a software developer.

The line answers the prompt "fortune cookie wisdom for developers".
Its idea is a quiet warning about legacy code: the code you ship
today will outlive the comments that explain it, and one day a
stranger will inherit both at 3 a.m. — and that stranger is you,
months from now, staring at your own forgotten logic. The fortune
works because it sounds like a proverb about kindness to strangers,
then the twist reveals the stranger is your future self, so the
advice is really self-preservation dressed as courtesy.

Gate guard: the entry must be UTF-8 text of 1 to 120 characters, a
single line, and not only white space - the same gate the sealed
scorer applies to /output/entry.txt. Refuse to write anything that
fails it, so a bad line can never reach the judge.

Note: the entry is written with no trailing newline, so the file
holds exactly the 120 characters of the line and nothing else.
"""

from pathlib import Path

ENTRY = (
    "Your code will outlive your comments. Write both as if a stranger "
    "inherits them at 3 a.m. — that stranger is future you."
)

MIN_CHARS = 1
MAX_CHARS = 120


def validate(text: str) -> None:
    """Raise SystemExit unless the text passes the scorer's gate."""
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
