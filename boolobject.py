class Bool(int):
    """Bool(x) -> bool

    Return True when the argument x is true, False otherwise.
    The builtins True and False are the only two instances of the class bool.
    The class bool is a subclass of the class int, and cannot be subclassed."""

    def __new__(cls, x=0, /):
        if x:
            return True
        else:
            return False

    def __repr__(self, /):
        if self:
            return "True"
        else:
            return "False"

    __str__ = __repr__

    def __and__(self, value, /):
        if isinstance(value, bool):
            return bool(int(self) & int(value))
        else:
            return int.__and__(self, value)

    __rand__ = __and__

    def __or__(self, value, /):
        if isinstance(value, bool):
            return bool(int(self) | int(value))
        else:
            return int.__or__(self, value)

    __ror__ = __or__

    def __xor__(self, value, /):
        if isinstance(value, bool):
            return bool(int(self) ^ int(value))
        else:
            return int.__xor__(self, value)

    __rxor__ = __xor__
