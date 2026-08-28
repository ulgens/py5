import argparse

import py5_tools.utilities

parser = argparse.ArgumentParser(description="Generate Py5Utilities framework")
parser.add_argument(
    "-o",
    "--output",
    action="store",
    dest="output_dir",
    help="output destination (defaults to current directory)",
)


def main(args=None):
    args = args or parser.parse_args()

    py5_tools.utilities.generate_utilities_framework(args.output_dir)


if __name__ == "__main__":
    main()
