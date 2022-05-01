from built_in_functions import MISSING, is_iter, verifier


class Set:
    """Set() -> new empty set object
    Set(iterable) -> new set object

    Build an unordered collection of unique elements."""

    def __init__(self, value=MISSING, /):
        self.__data = set()
        if isinstance(value, type(self.__data)):
            self.__data = value
        elif isinstance(value, self.__class__):
            self.__data = value.__data
        elif value is not MISSING:
            if not is_iter(value):
                raise TypeError(
                    f"'{type(value).__name__}' object is not iterable")

            for x in value:
                self.add(x)

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
        return value.__data if isinstance(value, Set) else value

    @verifier
    def __sub__(self, value, /):
        return self.difference(value)

    @verifier
    def __xor__(self, value, /):
        return self.symmetric_difference(value)

    @verifier
    def __ixor__(self, value, /):
        self.symmetric_difference_update(value)
        return self

    __rxor__ = __xor__

    @verifier
    def __and__(self, value, /):
        return self.intersection(value)

    @verifier
    def __iand__(self, value, /):
        self.intersection_update(value)
        return self

    __rand__ = __and__

    @verifier
    def __or__(self, value, /):
        return self.union(value)

    @verifier
    def __ior__(self, value, /):
        self.update(value)
        return self

    __ror__ = __or__

    def __iter__(self, /):
        return iter(self.__data)

    def __contains__(self, key, /):
        return key in self.__data

    def __len__(self, /):
        return len(self.__data)

    def __sizeof__(self, /):
        return self.__data.__sizeof__()

    def __repr__(self, /):
        return f"{self.__class__.__name__}({repr(self.__data)[1:-1]})"

    def __copy__(self, /):
        inst = self.__class__.__new__(self.__class__)
        inst.__dict__.update(self.__dict__)
        # Create a copy and avoid triggering descriptors
        inst.__dict__[f"_{self.__class__.__name__}__data"] = self.__dict__[
            f"_{self.__class__.__name__}__data"].copy()
        return inst

    def add(self, obj, /):
        """Add an element to a set.

        This has no effect if the element is already present."""

        return self.__data.add(obj)

    def update(self, value, /):
        "Update a set with the union of itself and others."

        for elem in value:
            self.add(elem)

    def copy(self, /):
        "Return a shallow copy of a Set."

        return self.__class__(self)

    def clear(self, /):
        "Remove all elements from this Set."

        self.__data.clear()

    def pop(self, /):
        """Remove and return an arbitrary set element.

        Raises KeyError if the set is empty."""

        if self.__data:
            return self.__data.pop()

        raise IndexError("pop from empty Set")

    def remove(self, key, /):
        """Remove an element from a set; it must be a member.

        If the element is not a member, raise a KeyError."""

        if key in self.__data:
            self.__data.remove(key)

        KeyError(key)

    def discard(self, key, /):
        """Remove an element from a set if it is a member.

        If the element is not a member, do nothing."""

        if key in self.__data:
            self.__data.remove(key)

    def union(self, value, /):  # other is any sequence
        """Return the union of sets as a new set.

        (i.e. all elements that are in either set.)"""

        res = self.copy()
        for x in value:
            if not x in res:
                res.add(x)
        return res

    def intersection(self, value, /):  # other is any sequence
        """Return the intersection of two sets as a new set.

       (i.e. all elements that are in both sets.)"""

        res = self.__class__()
        for x in self:
            if x in value:
                res.add(x)
        return res

    def intersection_update(self, value, /):
        "Update a set with the intersection of itself and another."

        res = set()
        for x in self:
            if x in value:
                res.add(x)
        self.__data = res

    def difference(self, value, /):
        """Return the difference of two or more sets as a new set.

        (i.e. all elements that are in this set but not the others.)"""

        res = self.copy()
        for x in value:
            if x in self:
                res.remove(x)
        return res

    def difference_update(self, value, /):
        "Remove all elements of another set from this set."

        for x in value:
            if x in self:
                self.remove(x)
        return self

    def symmetric_difference(self, value, /):
        """Return the symmetric difference of two sets as a new set.

        (i.e. all elements that are in exactly one of the sets.)"""

        res = self.copy()
        for x in value:
            if x in self:
                res.remove(x)
            else:
                res.add(x)
        return res

    def symmetric_difference_update(self, value, /):
        "Update a set with the symmetric difference of itself and another."

        for x in value:
            if x in self:
                self.remove(x)
            else:
                self.add(x)

    def isdisjoint(self, value, /):
        "Return True if two sets have a null intersection."

        for x in value:
            if x in self:
                return False
        return True

    def issubset(self, value, /):
        "Report whether another set contains this set."

        for x in self:
            if not x in value:
                return False
        return True

    def issuperset(self, value, /):
        "Report whether this set contains another set."

        for x in value:
            if not x in self:
                return False
        return True