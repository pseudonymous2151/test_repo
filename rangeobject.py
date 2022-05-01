from built_in_functions import Reversed, errorhandler


class Range:
    """Return a range that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.

    range(i, j) produces i, i+1, i+2, ..., j-1

    start defaults to 0, and stop is omitted!

    range(4) produces 0, 1, 2, 3

    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement)."""

    __slots__ = ['start', 'stop', 'step'] + ['_Range__data']

    def __init__(self, /, start, stop=0, step=1):
        if start != 0 and stop == 0:
            start, stop = stop, start

        if step == 0:
            raise ValueError("Range() arg 3 must not be zero")

        errorhandler("'%s' object cannot be interpreted as an integer",
                     [start, int], [stop, int], [step, int])

        object.__setattr__(self, 'start', start)
        object.__setattr__(self, 'stop', stop)
        object.__setattr__(self, 'step', step)

        sequence = ()
        if step > 0:
            while start < stop:
                sequence += (start,)
                start += step
        else:
            while start > stop:
                sequence += (start,)
                start += step

        object.__setattr__(self, '_Range__data', sequence)

    def __getattribute__(self, name, /):
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value, /):
        raise AttributeError("read only attribute")

    def __bool__(self, /):
        return bool(self._Range__data)

    def __eq__(self, value, /):
        if not isinstance(value, self.__class__):
            return False
        if len(self._Range__data) != len(value):
            return False
        if len(self._Range__data) == 0:
            return True
        if self.start != value.start:
            return False
        if self._Range__data[-1] == value[-1]:
            return True
        return False

    def __ne__(self, value, /):
        if not isinstance(value, self.__class__):
            return True
        if len(self._Range__data) != len(value):
            return True
        if len(self._Range__data) == 0:
            return False
        if self.start != value.start:
            return True
        if self._Range__data[-1] == value[-1]:
            return False
        return True

    def __contains__(self, key, /):
        return key in self._Range__data

    def __getitem__(self, key, /):
        try:
            return self._Range__data[key]
        except IndexError:
            raise IndexError("Range object index out of range") from None

    def __len__(self, /):
        return (self.stop - self.start) // self.step

    def __hash__(self, /):
        if len(self) == 0:
            return id(Range)
        return hash((len(self), self.start, self[-1]))

    def __reduce__(self, /):
        return self.__data.__reduce__()

    def __iter__(self, /):
        class iterator(object):
            def __init__(self, value, /):
                self.__data = value
                self.__index = -1

            def __iter__(self, /):
                return self

            def __next__(self, /):
                if self.__index >= len(self.__data)-1:
                    raise StopIteration

                self.__index += 1
                return self.__data[self.__index]

            def __repr__(self, /):
                return "<Range_iterator object at %s>" % str(
                    hex(id(self))).replace('x', 'x00000').upper()

        return iterator(self._Range__data)

    def __reversed__(self, /):
        class Reverse(Reversed):
            def __repr__(self, /):
                return "<Range_iterator object at %s>" % str(
                    hex(id(self))).replace('x', 'x00000').upper()

        return Reverse(self._Range__data)

    def __repr__(self, /):
        if self.step == 1:
            return f"Range({self.start}, {self.stop})"

        return f"Range({self.start}, {self.stop}, {self.step})"

    def count(self, value, /):
        "rangeobject.count(value) -> integer -- return number of occurrences of value"

        i, _count = 0, 0
        while i < len(self):
            if value == self._Range__data[i]:
                _count += 1
            i += 1
        return _count

    def index(self, value, /):
        "rangeobject.index(value) -> integer -- return index of value."

        i = 0
        while i < len(self):
            if value == self._Range__data[i]:
                return i
            i += 1

        raise ValueError(f"{value} is not in Range")