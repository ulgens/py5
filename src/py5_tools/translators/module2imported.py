import re
from pathlib import Path
from typing import Union

from . import util


def translate_token(token):
    return token[4:] if token.startswith("py5.") else token


def post_translate(code):
    code = re.sub(r"^import py5" + chr(36), "", code, flags=re.MULTILINE)
    code = re.sub(r"^run_sketch\([^)]*\)" + chr(36), "", code, flags=re.MULTILINE)

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
