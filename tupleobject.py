from built_in_functions import verifier


class Tuple:
    """Built-in immutable sequence re-implementation.

    If no argument is given, the constructor returns an empty tuple.
    If iterable is specified the tuple is initialized from iterable's items.

    If the argument is a tuple, the return value is the same object."""

    def __init__(self, iterable=(), /):
        self.__data = ()
        if iterable != ():
            if isinstance(iterable, type(self.__data)):
                self.__data = iterable
            elif isinstance(iterable, self.__class__):
                self.__data = iterable.__data
            else:
                self.__data = tuple(iterable)

    def __eq__(self, value, /):
        if not isinstance(value, self.__class__):
            return False
        return self.__data == self.__cast(value)

    def __ne__(self, value, /):
        if not isinstance(value, self.__class__):
            return True
        return self.__data != self.__cast(value)

    @verifier
    def __lt__(self, value, /):
        return self.__data < self.__cast(value)

    @verifier
    def __le__(self, value, /):
        return self.__data <= self.__cast(value)

    @verifier
    def __gt__(self, value, /):
        return self.__data > self.__cast(value)

    @verifier
    def __ge__(self, value, /):
        return self.__data >= self.__cast(value)

    def __cast(self, value, /):
        return value.__data if isinstance(value, self.__class__) else value

    @verifier
    def __add__(self, value, /):
        return self.__class__(self.__data + value.__data)

    @verifier
    def __radd__(self, value, /):
        return self.__class__(value.__data + self.__data)

    @verifier
    def __iadd__(self, value, /):
        self.__data += value.__data
        return self

    @verifier
    def __mul__(self, value, /):
        return self.__class__(self.__data * value)

    __rmul__ = __mul__

    @verifier
    def __imul__(self, value, /):
        self.__data *= value
        return self

    def __contains__(self, key, /):
        return key in self.__data

    def __len__(self, /):
        return len(self.__data)

    def __hash__(self, /):
        return hash(self.__data)

    def __getitem__(self, index, /):
        if isinstance(index, slice):
            return self.__class__(self.__data[index])

        return self.__data[index]

    def __repr__(self, /):
        if len(self.__data) == 1:
            return f"{self.__class__.__name__}({self.__data[0]})"
        return f"{self.__class__.__name__}{repr(self.__data)}"

    def count(self, value, /):
        "Return number of occurrences of value."

        _count = 0
        for elem in self.__data:
            if elem == value:
                _count += 1
        return _count

    def index(self, value, start=0, stop=9223372036854775807, /):
        """Return first index of value.

        Raises ValueError if the value is not present."""

        length = len(self.__data)
        if length < stop:
            stop = length

        for i in range(start, stop):
            if value == self[i]:
                return i

        name = self.__class__.__name__
        raise ValueError(
            f"{name}.index(x): x not in {name}")
