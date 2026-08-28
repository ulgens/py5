import re
import string
from pathlib import Path
from typing import Union

from . import util

CONSTANT_CHARACTERS = string.ascii_uppercase + string.digits + "_"

PY5_CLASS_LOOKUP = {
    "PApplet": "Sketch",
    "PFont": "Py5Font",
    "PGraphics": "Py5Graphics",
    "PImage": "Py5Image",
    "PShader": "Py5Shader",
    "PShape": "Py5Shape",
    "PSurface": "Py5Surface",
    "PVector": "Py5Vector",
}

SPECIAL_CASES = {
    "println": "print",
}


def translate_token(token):
    if all([c in CONSTANT_CHARACTERS for c in list(token)]):
        return token
    if re.match(r"0x[\da-fA-F]{2,}", token):
        return token
    elif (stem := token.replace("()", "")) in PY5_CLASS_LOOKUP:
        return token.replace(stem, PY5_CLASS_LOOKUP[stem])
    elif token in SPECIAL_CASES:
        return SPECIAL_CASES[token]
    elif token[0].isupper():
        return token
    else:
        token = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", token)
        token = re.sub("([a-z0-9])([A-Z])", r"\1_\2", token)
        return token.lower()


def translate_code(code):
    return util.translate_code(translate_token, code)


def translate_file(src: Union[str, Path], dest: Union[str, Path]):
    util.translate_file(translate_token, src, dest)


def translate_dir(src: Union[str, Path], dest: Union[str, Path], ext=".pyde"):
    util.translate_dir(translate_token, src, dest, ext)


__all__ = ["translate_token", "translate_code", "translate_file", "translate_dir"]


def __dir__():
    return __all__
