import re
import time
from pathlib import Path

from IPython.core.magic_arguments import MagicHelpFormatter


class CellMagicHelpFormatter(MagicHelpFormatter):
    def add_usage(self, usage, actions, groups, prefix="::\n\n  %%"):
        super(MagicHelpFormatter, self).add_usage(usage, actions, groups, prefix)


def fix_triple_quote_str(code):
    for m in re.finditer(r"\"\"\"[^\"]*\"\"\"", code):
        code = code.replace(m.group(), m.group().replace("\n    ", "\n"))
    return code


def wait(wait_time, sketch):
    end_time = time.time() + wait_time
    while time.time() < end_time and sketch.is_running:
        time.sleep(0.1)


def filename_check(filename):
    filename = Path(filename)
    if not filename.parent.exists():
        filename.parent.mkdir(parents=True)
    return filename


def variable_name_check(varname):
    return re.match(r"^[a-zA-Z_]\w*" + chr(36), varname)


__all__ = [
    "CellMagicHelpFormatter",
    "fix_triple_quote_str",
    "wait",
    "filename_check",
    "variable_name_check",
]
