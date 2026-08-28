from jpype import JClass, JInt

_Py5ColorHelper = JClass("py5.core.Py5ColorHelper")


class Py5Color(int):
    def __new__(cls, val, *, _creator_instance=None):
        color = super().__new__(cls, val)

        if _creator_instance is None:
            raise ValueError(
                "Py5Color must be created by calling py5.color(). Do not instantiate directly."
            )

        color._creator_instance = _creator_instance
        return color

    def __repr__(self):
        return str(self)

    def __str__(self):
        color_mode_name = (
            "CMAP"
            if hasattr(self._creator_instance, "_cmap")
            and self._creator_instance._cmap is not None
            else None
        )

        return str(
            _Py5ColorHelper.repr(
                self._creator_instance._instance, color_mode_name, JInt(self)
            )
        )
