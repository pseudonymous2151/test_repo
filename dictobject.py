from built_in_functions import MISSING, Reversed, verifier


class Dict:
    """Dict() -> new empty dictionary
    Dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    Dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    Dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  Dict(one=1, two=2)"""

    def __init__(self, value=MISSING, /, **kwargs):
        self.__data = {}
        if isinstance(value, type(self.__data)):
            self.__data = value
        elif isinstance(value, self.__class__):
            self.__data = value.__data
        else:
            self.update(value)
        if kwargs:
            self.update(kwargs)

    def __eq__(self, value, /):
        if not isinstance(value, self.__class__):
            return False
        return self.__data == value.__data

    def __ne__(self, value, /):
        if not isinstance(value, self.__class__):
            return True
        return self.__data != value.__data

    @verifier
    def __or__(self, value, /):
        return self.__class__(self.__data | value.__data)

    @verifier
    def __ror__(self, value, /):
        return self.__class__(value.__data | self.__data)

    @verifier
    def __ior__(self, value, /):
        self.__data |= value.__data
        return self

    def __getitem__(self, key, /):
        if key in self.__data:
            return self.__data[key]

        raise KeyError(key)

    def __setitem__(self, key, value, /):
        self.__data[key] = value

    def __delitem__(self, key, /):
        del self.__data[key]

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

    def copy(self, /):
        "D.copy() -> a shallow copy of D"

        return self.__class__(self)

    def clear(self, /):
        "D.clear() -> None.  Remove all items from D."

        self.__data.clear()

    def pop(self, key, default=None, /):
        """D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

        If the key is not found, return the default if given; otherwise,
        raise a KeyError."""

        if key in self.__data:
            return self.__data.pop(key)

        if default is not None:
            return default
        raise KeyError(key)

    def popitem(self, /):
        """Remove and return a (key, value) pair as a 2-tuple.

        Pairs are returned in LIFO (last-in, first-out) order.
        Raises KeyError if the dict is empty."""

        if not self.__data:
            raise KeyError("'popitem(): dictionary is empty'")

        key = list(self.__data)[-1]

        value = self.__data.pop(key)
        return (key, value)

    def setdefault(self, key, default=None, /):
        """Insert key with a value of default if key is not in the dictionary.

        Return the value for key if key is in the dictionary, else default."""

        if key in self.__data:
            return self.__data[key]

        self.__data[key] = default
        return default

    def update(self, value=MISSING, /, **kwargs):
        """D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]"""

        def copy(iterable, /):
            try:
                for k, v in iterable:
                    self.__data[k] = v
            except TypeError:
                raise TypeError(
                    "cannot convert dictionary update sequence element #0 to a sequence") from None

        if value is not MISSING:
            try:
                if hasattr(value, 'keys'):
                    kvs = ((k, value[k]) for k in value.keys())
                elif hasattr(value, 'items'):
                    kvs = value.items()
                elif isinstance(value, str):
                    raise ValueError
                elif iter(value):
                    kvs = value
                else:
                    raise TypeError
            except TypeError:
                raise TypeError(
                    f"'{type(value).__name__}' object is not iterable") from None
            except ValueError:
                raise ValueError(
                    "dictionary update sequence element #0 has length 1; 2 is required") from None
            copy(kvs)

        if kwargs:
            copy(kwargs.items())

    def get(self, key, default=None, /):
        "Return the value for key if key is in the dictionary, else default."

        if key in self.__data:
            return self.__data[key]

        return default

    @classmethod
    def fromkeys(cls, iterable, value=None, /):
        "Create a new dictionary with keys from iterable and values set to value."

        d = cls()
        for key in iterable:
            d[key] = value
        return d

    def keys(self, /):
        "D.keys() -> a set-like object providing a view on D's keys"

        class dict_keys:
            def __init__(self, value):
                self.__data = []
                for key in value:
                    self.__data.append(key)

            def __len__(self, /):
                return len(self.__data)

            def __iter__(self, /):
                return iter(self.__data)

            def __reversed__(self, /):
                class Reverse(Reversed):
                    def __repr__(self, /):
                        return "<dict_reversekeyiterator object at %s>" % str(
                            hex(id(self))).replace('x', 'x00000').upper()

                return Reverse(self.__data)

            def __repr__(self, /):
                return f"{self.__class__.__name__}({self.__data})"

        return dict_keys(self.__data)

    def values(self, /):
        "D.values() -> an object providing a view on D's values"

        class dict_values:
            def __init__(self, value, /):
                self.__data = []
                for key in value:
                    self.__data.append(value[key])

            def __len__(self, /):
                return len(self.__data)

            def __iter__(self, /):
                return iter(self.__data)

            def __reversed__(self, /):
                class Reverse(Reversed):
                    def __repr__(self, /):
                        return "<dict_reversevalueiterator object at %s>" % str(
                            hex(id(self))).replace('x', 'x00000').upper()

                return Reverse(self.__data)

            def __repr__(self, /):
                return f"{self.__class__.__name__}({self.__data})"

        return dict_values(self.__data)

    def items(self, /):
        "D.items() -> a set-like object providing a view on D's items"

        class dict_items:
            def __init__(self, value=MISSING, /):
                self.__data = []
                if value is not MISSING:
                    for key in value:
                        self.__data.append((key, value[key]))

            def __eq__(self, value, /):
                if not isinstance(value, self.__class__):
                    return False
                return self.__data == value.__data

            def __ne__(self, value, /):
                if not isinstance(value, self.__class__):
                    return True
                return self.__data != value.__data

            def __lt__(self, value, /):
                return self.__data < self.__cast(value, '<')

            def __le__(self, value, /):
                return self.__data <= self.__cast(value, '<=')

            def __gt__(self, value, /):
                return self.__data > self.__cast(value, '>')

            def __ge__(self, value, /):
                return self.__data >= self.__cast(value, '>=')

            def __cast(self, value, symbol, /):
                if hasattr(value, '_dict_items__data'):
                    return value.__data

                raise TypeError(
                    "unsupported operand type(s) for %s: '%s' and '%s'" % (
                        symbol, self.__class__.__name__, type(value).__name__))

            def __and__(self, value, /):
                res = set()
                for x in self:
                    if x in value:
                        res.add(x)
                return res

            __rand__ = __and__

            def __or__(self, value, /):
                res = set(self.__data)
                for x in value:
                    if not x in res:
                        res.add(x)
                return res

            __ror__ = __or__

            def __xor__(self, value, /):
                res = set(self.__data)
                for x in value:
                    if x in self:
                        res.remove(x)
                    else:
                        res.add(x)
                return res

            __rxor__ = __xor__

            def __sub__(self, value, /):
                res = set(self.__data)
                for x in value:
                    if x in self:
                        res.remove(x)
                return res

            __rsub__ = __sub__

            def __len__(self, /):
                return len(self.__data)

            def __iter__(self, /):
                return iter(self.__data)

            def __repr__(self, /):
                return f"{self.__class__.__name__}({self.__data})"

            def __reversed__(self, /):
                class Reverse(Reversed):
                    "Return a reverse iterator over the dict items."

                    def __repr__(self, /):
                        return "<dict_reverseitemiterator object at %s>" % str(
                            hex(id(self))).replace('x', 'x00000').upper()

                return Reverse(self.__data)

            def isdisjoint(self, value, /):
                "Return True if the view and the given iterable have a null intersection."

                for x in value:
                    if x in self:
                        return False
                return True

        return dict_items(self.__data)
