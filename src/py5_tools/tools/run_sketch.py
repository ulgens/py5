import argparse

from py5_tools import imported

parser = argparse.ArgumentParser(description="Execute py5 sketch")
parser.add_argument(action="store", dest="sketch_path", help="path to py5 sketch")
parser.add_argument(
    "-c",
    "--classpath",
    action="store",
    dest="classpath",
    help="extra directories to add to classpath",
)
parser.add_argument(
    "--py5-options",
    nargs="*",
    dest="py5_options",
    help='list of parameters to pass to Processing (do not prefix anything with a "-")',
)
parser.add_argument(
    "--sketch-args",
    nargs="*",
    dest="sketch_args",
    help='list of parameters to pass to py5 (do not prefix anything with a "-")',
)

# DEPRECATED PARAMETERS, --py5_options USED IN THONNY PLUGIN
parser.add_argument(
    "--py5_options",
    nargs="*",
    dest="py5_options",
    help='(DEPRECATED PARAMETER) list of parameters to pass to Processing (do not prefix anything with a "-")',
)
parser.add_argument(
    "--sketch_args",
    nargs="*",
    dest="sketch_args",
    help='(DEPRECATED PARAMETER) list of parameters to pass to py5 (do not prefix anything with a "-")',
)


def main(args=None):
    args = args or parser.parse_args()

    imported.run_code(
        args.sketch_path,
        classpath=args.classpath,
        py5_options=args.py5_options,
        sketch_args=args.sketch_args,
    )


if __name__ == "__main__":
    main()
