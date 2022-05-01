from built_in_functions import Reversed, Sorted, verifier


class List:
    """Built-in mutable sequence re-implementation.

    If no argument is given, the constructor creates a new empty list.
    The argument must be an iterable if specified."""

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

    def __sizeof__(self, /):
        return self.__data.__sizeof__()

    def __getitem__(self, index, /):
        if isinstance(index, slice):
            return self.__class__(self.__data[index])

        return self.__data[index]

    def __setitem__(self, index, value, /):
        if not self.__data or index > 0 and index > len(
                self)-1 or index < 0 and -index > len(self):
            raise IndexError(
                f"{self.__class__.__name__} assignment index out of range")

        if index < 0 and -index > len(self.__data)-1:
            index = 0

        if index < 0:
            index = len(self.__data) + index + 1

        self.__data = self.__data[:index] + (value,) + self.__data[index+1:]

    def __delitem__(self, key, /):
        if not self.__data or key > 0 and key > len(
                self)-1 or key < 0 and -key > len(self):
            raise IndexError(
                f"{self.__class__.__name__} assignment index out of range")

        if key < 0 and -key > len(self.__data)-1:
            key = 0

        if key < 0:
            key = len(self.__data) + key

        self.__data = self.__data[:key] + self.__data[key+1:]

    def __copy__(self, /):
        inst = self.__class__.__new__(self.__class__)
        inst.__dict__.update(self.__dict__)
        # Create a copy and avoid triggering descriptors
        inst.__dict__[f"_{self.__class__.__name__}__data"] = self.__dict__[
            f"_{self.__class__.__name__}__data"][:]
        return inst

    def __repr__(self, /):
        if len(self.__data) == 1:
            return f"{self.__class__.__name__}({self.__data[0]})"
        return f"{self.__class__.__name__}{repr(self.__data)}"

    def append(self, obj, /):
        "Append object to the end of the list."

        self.__data += (obj,)

    def insert(self, index, obj, /):
        "Insert object before index."

        if index < 0 and -index > len(self.__data)-1:
            index = 0

        if index < 0:
            index = len(self.__data) + index + 1

        self.__data = self.__data[:index] + (obj,) + self.__data[index:]

    def pop(self, index=-1, /):
        """Remove and return item at index (default last).

        Raises IndexError if list is empty or index is out of range."""

        if not self.__data:
            raise IndexError("pop from empty List")
        if index > 0 and index > len(self)-1 or index < 0 and -index > len(self):
            raise IndexError("pop index out of range")

        if index < 0:
            index = len(self.__data) + index

        element = self.__data[index]
        self.__data = self.__data[:index] + self.__data[index+1:]

        return element

    def remove(self, value, /):
        """Remove first occurrence of value.

        Raises ValueError if the value is not present."""

        for index in range(len(self.__data)):
            if value == self[index]:
                self.__data = self.__data[:index] + self.__data[index+1:]
                return None

        name = self.__class__.__name__
        raise ValueError(
            f"{name}.remove(x): x not in {name}")

    def clear(self, /):
        "Remove all items from list."

        self.__data = ()

    def copy(self, /):
        "Return a shallow copy of the list."

        return self.__class__(self)

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

        raise ValueError(
            f"'{value}' is not in {self.__class__.__name__}")

    def reverse(self, /):
        "Reverse *IN PLACE*."

        self.__data = tuple(Reversed(self.__data))

    def sort(self, /, *, key=None, reverse=False):
        """Sort the list in ascending order and return None.

        The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
        order of two equal elements is maintained).

        If a key function is given, apply it once to each list item and sort them,
        ascending or descending, according to their function values.

        The reverse flag can be set to sort in descending order."""

        self.__data = tuple(Sorted(self.__data, key=key, reverse=reverse))

    def extend(self, iterable, /):
        "Extend list by appending elements from the iterable."

        if isinstance(iterable, List):
            self.__data += iterable.__data
        else:
            for x in iterable:
                self.__data += (x,)
