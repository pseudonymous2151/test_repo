from sys import getdefaultencoding
from string_methods import *
from built_in_functions import verifier


class Str:
    """Str(bytes_or_buffer[, encoding[, errors]]) -> Str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'."""

    def __init__(self, obj='', /, *, encoding=getdefaultencoding(), errors='strict'):
        is_true = encoding == getdefaultencoding() and errors == 'strict'
        if isinstance(obj, str) and is_true:
            self.__data = obj
        elif isinstance(obj, Str) and is_true:
            self.__data = obj.__data[:]
        elif is_true:
            self.__data = str(obj)
        else:
            self.__data = str(obj, encoding, errors)

    def __str__(self, /):
        return f"{self.__class__.__name__}('{self.__data}')"

    def __repr__(self, /):
        return f"{self.__class__.__name__}({repr(self.__data)})"

    def __int__(self, /):
        return int(self.__data)

    def __float__(self, /):
        return float(self.__data)

    def __complex__(self, /):
        return complex(self.__data)

    def __hash__(self, /):
        return hash(self.__data)

    def __getnewargs__(self, /):
        return (self.__data[:],)

    def __len__(self, /):
        return len(self.__data)

    def __sizeof__(self, /):
        return self.__data.__sizeof__()

    def __getitem__(self, key, /):
        return self.__data[key]

    def __eq__(self, value, /):
        if not isinstance(value, self.__class__):
            return False
        return self.__data == value.__data

    def __ne__(self, value, /):
        if not isinstance(value, self.__class__):
            return True
        return self.__data != value.__data

    @verifier
    def __lt__(self, value, /):
        return self.__data < value.__data

    @verifier
    def __le__(self, value, /):
        return self.__data <= value.__data

    @verifier
    def __gt__(self, value, /):
        return self.__data > value.__data

    @verifier
    def __ge__(self, value, /):
        return self.__data >= value.__data

    def __contains__(self, value, /):
        if isinstance(value, Str):
            value = value.__data
        return value in self.__data

    @verifier
    def __add__(self, value, /):
        return self.__class__(self.__data + value.__data)

    @verifier
    def __radd__(self, value, /):
        return self.__class__(value.__data + self.__data)

    @verifier
    def __mul__(self, value, /):
        return self.__class__(self.__data * value)

    __rmul__ = __mul__

    def __mod__(self, value, /):
        return self.__class__(self.__data % value)

    def __rmod__(self, value, /):
        return self.__class__(value % self.__data)

    def __format__(self, format_spec, /):
        return self.__data.__format__(format_spec)

    maketrans = str.maketrans

    def translate(self, /, *args):
        """Replace each character in the string using the given translation table.

        table
          Translation table, which must be a mapping of Unicode ordinals to
          Unicode ordinals, strings, or None.

        The table must implement lookup/indexing via __getitem__, for instance a
        dictionary or list.  If this operation raises LookupError, the character is
        left untouched.  Characters mapped to None are deleted."""

        return self.__class__(self.__data.translate(*args))

    def encode(self, /, encoding='utf-8', errors='strict'):
        """Encode the string using the codec registered for encoding.

        encoding
            The encoding in which to encode the string.
        errors
            The error handling scheme to use for encoding errors.
            The default is 'strict' meaning that encoding errors raise a
            UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
            'xmlcharrefreplace' as well as any other name registered with
            codecs.register_error that can handle UnicodeEncodeErrors."""

        return self.__data.encode(encoding, errors)

    def format(self, /, *args, **kwds):
        """Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}')."""

        return self.__data.format(*args, **kwds)

    def format_map(self, /, mapping):
        """Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}')."""

        return self.__data.format_map(mapping)

    def isdigit(self, /):
        """Return True if the string is a digit string, False otherwise.

        A string is a digit string if all characters in the string are digits and there"""

        return self.__data.isdigit()

    def isascii(self, /):
        """Return True if all characters in the string are ASCII, False otherwise.

        ASCII characters have code points in the range U+0000-U+007F.
        Empty string is ASCII too."""

        return self.__data.isascii()

    def isnumeric(self, /):
        """Return True if the string is a numeric string, False otherwise.

        A string is numeric if all characters in the string are numeric and there is at
        least one character in the string."""

        return self.__data.isnumeric()

    def isidentifier(self, /):
        """Return True if the string is a valid Python identifier, False otherwise.

        Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
        such as "def" or "class"."""

        return self.__data.isidentifier()

    def casefold(self, /):
        "Return a version of the string suitable for caseless comparisons."

        return self.__class__(self.__data.casefold())

    def isdecimal(self, /):
        """Return True if the string is a decimal string, False otherwise.

        A string is a decimal string if all characters in the string are decimal and there is at least one character in the string."""

        return isdecimal(self.__data)

    def isalpha(self, /):
        """Returns True if the string is an alphabetic string, False otherwise.

        A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string."""

        return isalpha(self.__data)

    def isalnum(self, /):
        """Returns True if the string is an alphanumeric string, False otherwise.

        A string is alphanumeric if all characters in the string are alphanumeric and there is at least one character in the string."""

        return isalnum(self.__data)

    def islower(self, /):
        """Returns True if the string is a lowercase string, False otherwise.

        A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string."""

        return islower(self.__data)

    def isupper(self, /):
        """Returns True if the string is an uppercase string, False otherwise.

        A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string."""

        return isupper(self.__data)

    def istitle(self, /):
        """Returns a version of the string where each word is titlecased.

        More specifically, words start with uppercased characters and all remaining cased characters have lower case."""

        return istitle(self.__data)

    def isspace(self, /):
        """Returns True if the string is a whitespace string, False otherwise.

        A string is whitespace if all characters in the string are whitespace and there is at least one character in the string."""

        return isspace(self.__data)

    def isprintable(self, /):
        """Returns True if the string is printable, False otherwise.

        A string is printable if all of its characters are considered printable in repr() or if it is empty."""

        return isprintable(self.__data)

    def lower(self, /):
        "Returns a copy of the string converted to lowercase."

        return self.__class__(lower(self.__data))

    def upper(self, /):
        "Returns a copy of the string converted to uppercase."

        return self.__class__(upper(self.__data))

    def swapcase(self, /):
        "Converts uppercase characters to lowercase and lowercase characters to uppercase."

        return self.__class__(swapcase(self.__data))

    def capitalize(self, /):
        """Returns a capitalized version of the string.

        More specifically, make the first character have upper case and the rest lower case."""

        return self.__class__(capitalize(self.__data))

    def title(self, /):
        """Returns a version of the string where each word is titlecased.

        More specifically, words start with uppercased characters and all remaining cased characters have lower case."""

        return self.__class__(title(self.__data))

    def center(self, /, width, fillchar=" "):
        """Returns a centered string of length width.

        Padding is done using the specified fill character (default is a space)."""

        if isinstance(fillchar, self.__class__):
            fillchar = fillchar.__data
        return self.__class__(center(self.__data, width, fillchar))

    def ljust(self, /, width, fillchar=" "):
        """Returns a left-justified string of length width.

        Padding is done using the specified fill character (default is a space)."""

        if isinstance(fillchar, self.__class__):
            fillchar = fillchar.__data
        return self.__class__(ljust(self.__data, width, fillchar))

    def rjust(self, /, width, fillchar=" "):
        """Returns a right-justified string of length width.

        Padding is done using the specified fill character (default is a space)."""

        if isinstance(fillchar, self.__class__):
            fillchar = fillchar.__data
        return self.__class__(rjust(self.__data, width, fillchar))

    def zfill(self, /, width):
        """Pad a numeric string with zeros on the left, to fill a field of the given width.

        The string is never truncated."""

        return self.__class__(zfill(self.__data, width))

    def expandtabs(self, /, tabsize=8):
        """Returns a copy where all tab characters are expanded using spaces.

        If tabsize is not given, a tab size of 8 characters is assumed."""

        return self.__class__(expandtabs(self.__data, tabsize))

    def partition(self, /, sep):
        """Partition the string into three parts using the given separator.
        This will search for the separator in the string.  If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it. If the separator is not found,
        returns a 3-tuple containing the original string and two empty strings."""

        if isinstance(sep, self.__class__):
            sep = sep.__data
        return partition(self.__data, sep)

    def rpartition(self, /, sep):
        """Partition the string into three parts using the given separator.
        This will search for the separator in the string, starting at the end.
        If the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it. If the separator is not found,
        returns a 3-tuple containing two empty strings and the original string."""

        if isinstance(sep, self.__class__):
            sep = sep.__data
        return rpartition(self.__data, sep)

    def splitlines(self, /, keepends=False):
        """Returns a list of the lines in the string, breaking at line boundaries.

        Line breaks are not included in the resulting list unless keepends is given and true."""

        return splitlines(self.__data, keepends)

    def removeprefix(self, /, prefix):
        """Returns a str with the given prefix string removed if present.

        If the string starts with the prefix string, return string[len(prefix):].
        Otherwise, return a copy of the original string."""

        if isinstance(prefix, self.__class__):
            prefix = prefix.__data
        return self.__class__(removeprefix(self.__data, prefix))

    def removesuffix(self, /, suffix):
        """Returns a str with the given suffix string removed if present.

        If the string ends with the suffix string and that suffix is not empty,
        return string[:-len(suffix)]. Otherwise, return a copy of the original string."""

        if isinstance(suffix, self.__class__):
            suffix = suffix.__data
        return self.__class__(removesuffix(self.__data, suffix))

    def startswith(self, /, prefix, start=0, end=None):
        """Returns True if self starts with the specified prefix, False otherwise.

        With optional start, test self beginning at that position.
        With optional end, stop comparing self at that position.
        Prefix can also be a tuple of strings to try."""
        if isinstance(prefix, self.__class__):
            prefix = prefix.__data
        return startswith(self.__data, prefix, start, end)

    def endswith(self, /, suffix, start=0, end=None):
        """Returns True if self ends with the specified suffix, False otherwise.
        With optional start, test self beginning at that position.
        With optional end, stop comparing self at that position.
        suffix can also be a tuple of strings to try."""

        if isinstance(suffix, self.__class__):
            suffix = suffix.__data
        return endswith(self.__data, suffix, start, end)

    def find(self, /, sub, start=0, end=None):
        """Returns the lowest index in self where substring sub is found,
        such that sub is contained within self[start:end].
        Optional arguments start and end are interpreted as in slice notation.
        Returns -1 on failure."""

        if isinstance(sub, self.__class__):
            sub = sub.__data
        return find(self.__data, sub, start, end)

    def rfind(self, /, sub, start=0, end=None):
        """Returns the highest index in self where substring sub is found,
        such that sub is contained within self[start:end].
        Optional arguments start and end are interpreted
        as in slice notation. Returns -1 on failure."""

        if isinstance(sub, self.__class__):
            sub = sub.__data
        return rfind(self.__data, sub, start, end)

    def index(self, /, sub, start=0, end=None):
        """Returns the lowest index in self where substring sub is found,
        such that sub is contained within self[start:end].
        Optional arguments start and end are interpreted as in slice notation.
        Raises ValueError when the substring is not found."""

        if isinstance(sub, self.__class__):
            sub = sub.__data
        return index(self.__data, sub, start, end)

    def rindex(self, /,  sub, start=0, end=None):
        """Returns the highest index in self where substring sub is found,
        such that sub is contained within self[start:end].
        Optional arguments start and end are interpreted as in slice notation.
        Raises ValueError when the substring is not found."""

        if isinstance(sub, self.__class__):
            sub = sub.__data
        return rindex(self.__data, sub, start, end)

    def count(self, /, sub, start=0, end=None):
        """Returns the number of non-overlapping occurrences of substring sub in string self[start:end].

        Optional arguments start and end are interpreted as in slice notation."""

        if isinstance(sub, self.__class__):
            sub = sub.__data
        return count(self.__data, sub, start, end)

    def join(self, /, iterable):
        """Concatenate any number of strings.

        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.

        Example: join('.', ['ab', 'pq', 'rs']) -> 'ab.pq.rs'"""

        return self.__class__(join(self.__data, iterable))

    def replace(self, /, old, new, maxsplit=-1):
        """Returns a copy with all occurrences of substring old replaced by new.
        count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.

        If the optional argument count is given, only the first count occurrences are replaced."""

        if isinstance(old, self.__class__):
            old = old.__data
        if isinstance(new, self.__class__):
            new = new.__data
        return self.__class__(replace(self.__data, old, new, maxsplit))

    def strip(self, /, chars=None):
        """Returns a copy of the string S with leading and trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead."""

        if isinstance(chars, self.__class__):
            chars = chars.__data
        return self.__class__(strip(self.__data, chars))

    def lstrip(self, /, chars=None):
        """Returns a copy of the string self with leading whitespace removed.

        If chars is given and not None, remove characters in chars instead."""

        if isinstance(chars, self.__class__):
            chars = chars.__data
        return self.__class__(lstrip(self.__data, chars))

    def rstrip(self, /, chars=None):
        """Returns a copy of the string self with trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead."""

        if isinstance(chars, self.__class__):
            chars = chars.__data
        return self.__class__(rstrip(self.__data, chars))

    def split(self, /, sep=None, maxsplit=-1):
        """Returns a list of the words in the string, using sep as the delimiter string.
        sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
        maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """

        if isinstance(sep, self.__class__):
            sep = sep.__data
        return split(self.__data, sep, maxsplit)

    def rsplit(self, /, sep=None, maxsplit=-1):
        """Returns a list of the words in the string, using sep as the delimiter string.
        sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
        maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """

        if isinstance(sep, self.__class__):
            sep = sep.__data
        return rsplit(self.__data, sep, maxsplit)