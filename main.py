# Write the one-line roast for the make.fun scorer.
import os
from pathlib import Path


TEXT = "My photo app made a slideshow called 'Together' starring my passport photo and a close-up of a rash."


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
