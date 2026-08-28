import os
import re
from pathlib import Path
from typing import Union

from .. import reference
from . import util


def translate_token(token):
    return "py5." + token if token in reference.PY5_DIR_STR else token


def post_translate(code):
    if not re.findall(r"^import py5" + chr(36), code, flags=re.MULTILINE):
        code = "import py5" + (3 * os.linesep) + code
    if not re.findall(r"^run_sketch\([^)]*\)" + chr(36), code, flags=re.MULTILINE):
        code += (3 * os.linesep) + "py5.run_sketch()" + os.linesep

    return code


def translate_code(code):
    return util.translate_code(translate_token, code, post_translate=post_translate)


def translate_file(src: Union[str, Path], dest: Union[str, Path]):
    util.translate_file(translate_token, src, dest, post_translate=post_translate)


def translate_dir(src: Union[str, Path], dest: Union[str, Path], ext=".py"):
    util.translate_dir(translate_token, src, dest, ext, post_translate=post_translate)


__all__ = ["translate_token", "translate_code", "translate_file", "translate_dir"]


def __dir__():
    return __all__
