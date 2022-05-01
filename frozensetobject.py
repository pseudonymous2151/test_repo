from built_in_functions import MISSING, verifier


class Frozenset:
    """Frozenset() -> empty Frozenset object
    Frozenset(iterable) -> Frozenset object

    Build an immutable unordered collection of unique elements."""

    def __init__(self, value=MISSING, /):
        self.__data = frozenset()
        if isinstance(value, type(self.__data)):
            self.__data = value
        elif isinstance(value, self.__class__):
            self.__data = value.__data
        elif value is not MISSING:
            self.__data = frozenset(value)

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
    def __sub__(self, value, /):
        return self.difference(value)

    @verifier
    def __xor__(self, value, /):
        return self.symmetric_difference(value)

    __rxor__ = __xor__

    @verifier
    def __and__(self, value, /):
        return self.intersection(value)

    __rand__ = __and__

    @verifier
    def __or__(self, value, /):
        return self.union(value)

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
        return repr(self.__data).capitalize()

    def copy(self, /):
        "Return a shallow copy of a Set."

        return self.__class__(self)

    def __copy__(self, /):
        inst = self.__class__.__new__(self.__class__)
        inst.__dict__.update(self.__dict__)
        # Create a copy and avoid triggering descriptors
        inst.__dict__[f"_{self.__class__.__name__}__data"] = self.__dict__[
            f"_{self.__class__.__name__}__data"].copy()
        return inst

    def union(self, value, /):  # other is any sequence
        """Return the union of sets as a new set.

        (i.e. all elements that are in either set.)"""

        new = set()
        for x in value:
            if not x in self:
                new.add(x)
        return self.__class__(new)

    def intersection(self, value, /):  # other is any sequence
        """Return the intersection of two sets as a new set.

       (i.e. all elements that are in both sets.)"""

        res = set()
        for x in self:
            if x in value:
                res.add(x)
        return self.__class__(res)

    def difference(self, value, /):
        """Return the difference of two or more sets as a new set.

        (i.e. all elements that are in this set but not the others.)"""

        res = set(self)
        for x in value:
            if x in self:
                res.remove(x)
        return self.__class__(res)

    def symmetric_difference(self, value, /):
        """Return the symmetric difference of two sets as a new set.

        (i.e. all elements that are in exactly one of the sets.)"""

        res = set(self)
        for x in value:
            if x in self:
                res.remove(x)
            else:
                res.add(x)
        return self.__class__(res)

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