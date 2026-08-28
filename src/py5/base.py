from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from py5.sketch import _Sketch


__all__ = ("Py5Base",)


class Py5Base:
    def __init__(self, instance: "_Sketch"):
        self._instance: "_Sketch" = instance

    def _shutdown(self):
        self._shutdown_complete = True

    def _replace_instance(self, new_instance: "_Sketch"):
        self._instance: "_Sketch" = new_instance
