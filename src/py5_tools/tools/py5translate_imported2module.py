import argparse
from pathlib import Path

from py5_tools import translators

parser = argparse.ArgumentParser(
    description="Translate imported mode code to module mode code"
)
parser.add_argument(action="store", dest="src", help="path to imported mode code")
parser.add_argument(action="store", dest="dest", help="path to module mode code")


def main(args=None):
    args = args or parser.parse_args()

    src = Path(args.src)
    dest = Path(args.dest)

    if not src.exists():
        print(f"Error: Code source {src} does not exist")
        return

    if src.is_dir() and (dest.is_dir() or not dest.exists()):
        translators.imported2module.translate_dir(src, dest)
    elif src.is_file() and (dest.is_file() or not dest.exists()):
        translators.imported2module.translate_file(src, dest)
    else:
        print("Error: The two arguments must both be directories or both be files")


if __name__ == "__main__":
    main()
