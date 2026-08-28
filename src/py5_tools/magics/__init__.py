import sys

from .drawing import DrawingMagics, DXFDrawingMagic


def load_ipython_extension(ipython):
    ipython.register_magics(DrawingMagics)
    if sys.platform != "darwin":
        ipython.register_magics(DXFDrawingMagic)
