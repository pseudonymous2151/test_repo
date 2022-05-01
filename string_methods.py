r"""This Module is re-implementation of python existing string methods
as functions on the basis of their execution output it's written
to Imitate those methods, it's not intended to be used in programs.

# Note: This module doesn't support unicode characters.
# Note: This module is a support file for stringobject.py

"""

# List of all string methods written within this module.
__all__ = ["isupper", "islower", "isalpha", "isdecimal", "isalnum", "isspace", "istitle",
           "isprintable", "startswith", "endswith", "removeprefix", "removesuffix", "upper",
           "lower", "swapcase", "title", "capitalize", "zfill", "ljust", "rjust", "center",
           "expandtabs", "partition", "rpartition", "splitlines", "find", "rfind", "index",
           "rindex", "count", "join", "replace", "strip", "lstrip", "rstrip", "split", "rsplit"]

"""A collection of string constants.

Public module variables:

whitespace -- a string containing all ASCII whitespace
ascii_lowercase -- a string containing all ASCII lowercase letters
ascii_uppercase -- a string containing all ASCII uppercase letters
ascii_letters -- a string containing all ASCII letters
digits -- a string containing all ASCII decimal digits
hexdigits -- a string containing all ASCII hexadecimal digits
octdigits -- a string containing all ASCII octal digits
punctuation -- a string containing all ASCII punctuation characters
printable -- a string containing all ASCII characters considered printable

"""

whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + ' '
ascii_letters_pairs = dict(zip(ascii_lowercase, ascii_uppercase))


def getkey(dct: dict, value: str) -> str:
    "Returns key for the value."

    for key, item in dct.items():
        if value == item:
            return key
    raise KeyError(f"key not found for {value}")


def errorhandler(*args, message=None) -> None:
    "Raises Type Error based on the arguments passed to it."

    if not message:
        message = "expected {} found {}"
    for value, datatype in args:
        if not isinstance(value, datatype):
            raise TypeError(
                message.format(datatype.__name__, type(value).__name__))


def islower(text):
    """Returns True if the string is a lowercase string, False otherwise.

    A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string."""

    errorhandler([text, str])

    is_true = False
    for letters in text:
        if letters in ascii_letters:
            if letters in ascii_uppercase:
                return False
            if not is_true:
                is_true = True

    return is_true


def isupper(text):
    """Returns True if the string is an uppercase string, False otherwise.

    A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string."""

    errorhandler([text, str])

    is_true = False
    for letters in text:
        if letters in ascii_letters:
            if letters in ascii_lowercase:
                return False
            if not is_true:
                is_true = True

    return is_true


def isalpha(text):
    """Returns True if the string is an alphabetic string, False otherwise.

    A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string."""

    errorhandler([text, str])

    if len(text) == 0:
        return False

    for i in text:
        if not i in ascii_letters:
            return False
    return True


def isdecimal(text):
    """Return True if the string is a decimal string, False otherwise.

    A string is a decimal string if all characters in the string are decimal and there is at least one character in the string."""

    errorhandler([text, str])

    if len(text) == 0:
        return False

    for i in text:
        if i not in digits:
            return False
    return True


def isalnum(text):
    """Returns True if the string is an alphanumeric string, False otherwise.

    A string is alphanumeric if all characters in the string are alphanumeric and there is at least one character in the string."""

    errorhandler([text, str])

    if len(text) == 0:
        return False

    ascii_alphanumeric = ascii_letters + digits
    for i in text:
        if i not in ascii_alphanumeric:
            return False
    return True


def istitle(text):
    """Returns a version of the string where each word is titlecased.

    More specifically, words start with uppercased characters and all remaining cased characters have lower case."""

    errorhandler([text, str])

    is_true = True
    is_title = False
    for i in text:
        if i in ascii_letters:
            if is_true:
                if i in ascii_lowercase:
                    return False
                if not is_title:
                    is_title = True
            elif not i in ascii_lowercase:
                return False
            is_true = False
        else:
            is_true = True

    return is_title


def isspace(text):
    """Returns True if the string is a whitespace string, False otherwise.

    A string is whitespace if all characters in the string are whitespace and there is at least one character in the string."""

    errorhandler([text, str])

    if len(text) == 0:
        return False

    for i in text:
        if i not in whitespace:
            return False
    return True


def isprintable(text):
    """Returns True if the string is printable, False otherwise.

    A string is printable if all of its characters are considered printable in repr() or if it is empty."""

    errorhandler([text, str])

    for i in text:
        if i not in printable:
            return False
    return True


def lower(text):
    "Returns a copy of the string converted to lowercase."

    errorhandler([text, str])

    string = ""
    for i in text:
        if i in ascii_letters:
            if i in ascii_lowercase:
                string += i
            else:
                string += getkey(ascii_letters_pairs, i)
        else:
            string += i
    return string


def upper(text):
    "Returns a copy of the string converted to uppercase."

    errorhandler([text, str])

    string = ""
    for i in text:
        if i in ascii_letters:
            if i in ascii_uppercase:
                string += i
            else:
                string += ascii_letters_pairs[i]
        else:
            string += i
    return string


def swapcase(text):
    "Converts uppercase characters to lowercase and lowercase characters to uppercase."

    errorhandler([text, str])

    string = ""
    for i in text:
        if i in ascii_letters:
            if i in ascii_lowercase:
                string += ascii_letters_pairs[i]
            else:
                string += getkey(ascii_letters_pairs, i)
        else:
            string += i
    return string


def capitalize(text):
    """Returns a capitalized version of the string.

    More specifically, make the first character have upper case and the rest lower case."""

    errorhandler([text, str])

    string = upper(text[0])
    for i in text[1:]:
        string += lower(i)
    return string


def title(text):
    """Returns a version of the string where each word is titlecased.

    More specifically, words start with uppercased characters and all remaining cased characters have lower case."""

    errorhandler([text, str])

    string, is_true = "", True
    for i in text:
        if i in ascii_letters:
            if is_true:
                if i in ascii_lowercase:
                    string += upper(i)
                else:
                    string += i
            else:
                string += lower(i)
            is_true = False
        else:
            is_true = True
            string += i
    return string


def ljust(text, width, fillchar=" "):
    """Returns a left-justified string of length width.

    Padding is done using the specified fill character (default is a space)."""

    errorhandler([text, str], [width, int], [fillchar, str])

    n_allign = width - len(text)
    return text + fillchar * n_allign


def rjust(text, width, fillchar=" "):
    """Returns a right-justified string of length width.

    Padding is done using the specified fill character (default is a space)."""

    errorhandler([text, str], [width, int], [fillchar, str])

    n_allign = width - len(text)
    return fillchar * n_allign + text


def center(text, width, fillchar=" "):
    """Returns a centered string of length width.

    Padding is done using the specified fill character (default is a space)."""

    errorhandler([text, str], [width, int], [fillchar, str])

    n_allign = width - len(text)
    return (fillchar * (n_allign if n_allign == 1 else n_allign // 2)) + text + (fillchar * (n_allign // 2))


def zfill(text, width):
    """Pad a numeric string with zeros on the left, to fill a field of the given width.

    The string is never truncated."""

    errorhandler([text, str], [width, int])

    n_zero = width - len(text) if width > 1 else 0
    if text[0] == "+":
        sign = "+"
    elif text[0] == "-":
        sign = "-"
    else:
        sign = ""

    return sign + "0" * n_zero + (text if sign == "" else text[1:])


def expandtabs(text, tabsize=8):
    """Returns a copy where all tab characters are expanded using spaces.

    If tabsize is not given, a tab size of 8 characters is assumed."""

    errorhandler([text, str], [tabsize, int])

    string = ""
    for s in text:
        if s == "\t":
            string += " " * tabsize
        else:
            string += s
    return string


def partition(text, sep):
    """Partition the string into three parts using the given separator.
    This will search for the separator in the string.  If the separator is found,
    returns a 3-tuple containing the part before the separator, the separator
    itself, and the part after it. If the separator is not found,
    returns a 3-tuple containing the original string and two empty strings."""

    errorhandler([text, str], [sep, str])

    len_sep = len(sep)
    for i in range(len(text)):
        if sep == text[i: i+len_sep]:
            return (text[0: i], text[i: i+len_sep], text[i+len_sep:])

    return (text, '', '')


def rpartition(text, sep):
    """Partition the string into three parts using the given separator.
    This will search for the separator in the string, starting at the end.
    If the separator is found, returns a 3-tuple containing the part before the
    separator, the separator itself, and the part after it. If the separator is not found,
    returns a 3-tuple containing two empty strings and the original string."""

    errorhandler([text, str], [sep, str])

    len_sep = len(sep)
    for i in reversed(range(len(text))):
        if sep == text[i: i+len_sep]:
            return (text[0: i], text[i: i+len_sep], text[i+len_sep:])

    return (text, '', '')


def splitlines(text, keepends=False):
    """Returns a list of the lines in the string, breaking at line boundaries.

    Line breaks are not included in the resulting list unless keepends is given and true."""

    errorhandler([text, str], [keepends, bool])

    line_breaks = "\n\r\v\f"
    string, output = "", []
    for s in text:
        if s in line_breaks:
            if keepends:
                output.append(string+s)
            else:
                output.append(string)
            # emptying the `string` variable
            # to clear previous stored strings
            string = ""
        else:
            string += s

    if text and s not in line_breaks:
        output.append(string)
    return output


def removeprefix(text, prefix):
    """Returns a str with the given prefix string removed if present.

    If the string starts with the prefix string, return string[len(prefix):].
    Otherwise, return a copy of the original string."""

    errorhandler([text, str], [prefix, str],
                 message="removeprefix() argument must be str, not {1}")

    if prefix not in text:
        return text

    sep = tuple(prefix)
    i, s_len = 0, len(text)
    while i < s_len and startswith(text[i], sep):
        i += 1

    return text[i: s_len]


def removesuffix(text, suffix):
    """Returns a str with the given suffix string removed if present.

    If the string ends with the suffix string and that suffix is not empty,
    return string[:-len(suffix)]. Otherwise, return a copy of the original string."""

    errorhandler([text, str], [suffix, str],
                 message="removesuffix() argument must be str, not {1}")

    if suffix not in text:
        return text

    sep = tuple(suffix)
    j = len(text)-1
    while 1 < j and startswith(text[j], sep):
        j -= 1

    return text[0: j+1]


def startswith(text, prefix, start=0, end=None):
    """Returns True if text starts with the specified prefix, False otherwise.

    With optional start, test text beginning at that position.
    With optional end, stop comparing text at that position.
    Prefix can also be a tuple of strings to try."""

    errorhandler([text, str], [start, int])
    if end is not None: errorhandler([end, int])
    if not isinstance(prefix, str):
        if isinstance(prefix, tuple):
            for _p in prefix:
                if not isinstance(_p, str):
                    raise TypeError(
                        f"tuple for startswith must only contain str, not {type(_p).__name__}")
        else:
            raise TypeError(
                f"startswith second arg must be str or a tuple of str, not {type(prefix).__name__}")

    if end is None: end = len(text)
    if isinstance(prefix, str):
        p_len = len(prefix)
        for i in range(start, end):
            if prefix == text[i: i+p_len]:
                return True
            else:
                return False
    else:
        for p in prefix:
            if p in text[start: end]:
                return True
        return False


def endswith(text, suffix, start=0, end=None):
    """Returns True if text ends with the specified suffix, False otherwise.
    With optional start, test text beginning at that position.
    With optional end, stop comparing text at that position.
    suffix can also be a tuple of strings to try."""

    errorhandler([text, str], [start, int])
    if end is not None: errorhandler([end, int])
    if not isinstance(suffix, str):
        if isinstance(suffix, tuple):
            for _s in suffix:
                if not isinstance(_s, str):
                    raise TypeError(
                        f"tuple for endswith must only contain str, not {type(_s).__name__}")
        else:
            raise TypeError(
                f"endswith second arg must be str or a tuple of str, not {type(suffix).__name__}")

    if end is None: end = len(text)
    if isinstance(suffix, str):
        s_len = len(suffix)
        for i in reversed(range(start, end+1)):
            if suffix == text[i-s_len: i]:
                return True
            else:
                return False
    else:
        is_true = False
        for s in suffix:
            if s in text[start: end]:
                if not is_true:
                    is_true = True
            else:
                return False
        return is_true


def find(text, sub, start=0, end=None):
    """Returns the lowest index in text where substring sub is found,
    such that sub is contained within text[start:end].
    Optional arguments start and end are interpreted as in slice notation.
    Returns -1 on failure."""

    errorhandler([text, str], [sub, str], [start, int])
    if end is not None: errorhandler([end, int])

    if end is None:
        end = len(text)
    s_len = len(sub)
    if s_len == 0:
        return 0

    for i in range(start, end):
        if sub == text[i: i+s_len]:
            return i
    return -1


def rfind(text, sub, start=0, end=None):
    """Returns the highest index in text where substring sub is found,
    such that sub is contained within text[start:end].
    Optional arguments start and end are interpreted
    as in slice notation. Returns -1 on failure."""

    errorhandler([text, str], [sub, str], [start, int])
    if end is not None: errorhandler([end, int])
    if sub == "" and text == "":
        return 0

    if end is None:
        end = len(text)
    s_len = len(sub)
    for i in reversed(range(start, end+1)):
        if sub == text[i: i+s_len]:
            if len(sub) != 0:
                return i
            return i + 1
    return -1


def index(text, sub, start=0, end=None):
    """Returns the lowest index in text where substring sub is found,
    such that sub is contained within text[start:end].
    Optional arguments start and end are interpreted as in slice notation.
    Raises ValueError when the substring is not found."""

    errorhandler([start, int])
    if end is not None: errorhandler([end, int])

    if end is None: end = len(text)
    if isinstance(text, str):
        s_len = len(sub)
        if s_len == 0:
            return 0

        for i in range(start, end):
            if sub == text[i: i+s_len]:
                return i

        raise ValueError("substring not found")
    else:
        if not hasattr(text, '__getitem__'):
            raise TypeError(
                f"'{type(text).__name__}' object is not subscriptable")

        for i in range(start, end):
            if sub == text[i]:
                return i

        raise ValueError(f"'{sub}' is not in {type(text).__name__}")


def rindex(text, sub, start=0, end=None):
    """Returns the highest index in text where substring sub is found,
    such that sub is contained within text[start:end].
    Optional arguments start and end are interpreted as in slice notation.
    Raises ValueError when the substring is not found."""

    errorhandler([text, str], [sub, str], [start, int])
    if end is not None: errorhandler([end, int])
    if sub == "" and text == "":
        return 0

    if end is None:
        end = len(text)
    len_sub = len(sub)
    for i in reversed(range(start, end)):
        if sub == text[i: i+len_sub]:
            if len(sub) != 0:
                return i
            return i + 1

    raise ValueError("substring not found")


def count(text, sub, start=0, end=None):
    """Returns the number of non-overlapping occurrences of substring sub in string text[start:end].

    Optional arguments start and end are interpreted as in slice notation."""

    errorhandler([start, int])
    if end is not None: errorhandler([end, int])
    iter(text)  # Raises error for non iterables

    if end is None: end = len(text)
    _count = 0 # holds substring occurrences
    if isinstance(text, str):
        #! issue with counting empty string
        #! returns wrong result for this case
        s_len = len(sub)
        for i in range(start, end):
            if sub == text[i: i+s_len]:
                _count += 1

        if len(sub) != 0:
            return _count
        return _count + 1
    else:
        for i in range(start, end):
            if sub == text[i]:
                _count += 1
        return _count


def join(text, iterable):
    """Concatenate any number of strings.

    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.

    Example: join('.', ['ab', 'pq', 'rs']) -> 'ab.pq.rs'"""

    errorhandler([text, str])
    it = iter(iterable)  # Raises error for non iterables

    output = ""
    for s in it:
        output += s + text
    return output


def replace(text, old, new, count=-1):
    """Returns a copy with all occurrences of substring old replaced by new.
    count
       Maximum number of occurrences to replace.
       -1 (the default value) means replace all occurrences.

    If the optional argument count is given, only the first count occurrences are replaced."""

    # Checks for valid arguments and raises error if not valid
    errorhandler([text, str], [old, str], [new, str], [count, int])

    is_true = True if count <= -1 else False
    string, old_len = "", len(old)
    for idx, item in enumerate(text):
        if old == text[idx: idx+old_len]:
            if 0 < count or is_true:
                string += new
                idx += old_len-1
                count -= 1
            else:
                string += item
        else:
            string += item
    return string


LEFTSTRIP = 0
RIGHSTRIP = 1
BOTHSTRIP = 2


def do_strip(text, striptype):
    i = 0
    if striptype != RIGHSTRIP:
        while i < len(text) and isspace(text[i]):
            i += 1

    j = len(text)-1
    if striptype != LEFTSTRIP:
        while (1 < j and isspace(text[j])):
            j -= 1

    return text[i: j+1]


def do_argstrip(text, striptype, chars):
    sep = tuple(chars)
    i = 0
    if striptype != RIGHSTRIP:
        while i < len(text) and startswith(text[i], sep):
            i += 1

    j = len(text)-1
    if striptype != LEFTSTRIP:
        while 1 < j and startswith(text[j], sep):
            j -= 1

    return text[i: j+1]


def strip(text, chars=None):
    """Returns a copy of the string S with leading and trailing whitespace removed.

    If chars is given and not None, remove characters in chars instead."""

    errorhandler([text, str])
    if chars is not None:
        errorhandler([chars, str])

    if chars is None:
        return do_strip(text, BOTHSTRIP)
    else:
        return do_argstrip(text, BOTHSTRIP, chars)


def lstrip(text, chars=None):
    """Returns a copy of the string text with leading whitespace removed.

    If chars is given and not None, remove characters in chars instead."""

    errorhandler([text, str])
    if chars is not None:
        errorhandler([chars, str])

    if chars is None:
        return do_strip(text, LEFTSTRIP)
    else:
        return do_argstrip(text, LEFTSTRIP, chars)


def rstrip(text, chars=None):
    """Returns a copy of the string text with trailing whitespace removed.

    If chars is given and not None, remove characters in chars instead."""

    errorhandler([text, str])
    if chars is not None:
        errorhandler([chars, str])

    if chars is None:
        return do_strip(text, RIGHSTRIP)
    else:
        return do_argstrip(text, RIGHSTRIP, chars)


def do_split(text, split_type, maxsplit=-1):
    is_true = True if maxsplit <= -1 else False
    string, indexes, output = "", (), []

    i = 0
    if split_type == LEFTSTRIP:
        text = lstrip(text)
        j = len(text)-1
        while i < len(text):
            if isspace(text[i]):
                if 0 < maxsplit or is_true:
                    indexes += (i,)
                    if i < j and not isspace(text[i+1]):
                        maxsplit -= 1
            i += 1
    else:
        text = rstrip(text)
        j = len(text)-1
        while j > -1:
            if isspace(text[j]):
                if 0 < maxsplit or is_true:
                    indexes += (j,)
                    if j > 0 and not isspace(text[j-1]):
                        maxsplit -= 1
            j -= 1
    idx = 0
    while idx < len(text):
        if idx in indexes:
            output.append(string)
            # Emptying the `string` variable
            # to clear pervious stored strings
            string = ""
        else:
            string += text[idx]
        idx += 1
    output.append(string)
    # removing all whitespace elements
    out = [x for x in output if x != ""]
    # removing extra whitespaces of the elements
    if split_type == LEFTSTRIP:
        return [lstrip(x) for x in out]
    else:
        return [rstrip(x) for x in out]


def do_argsplit(text, split_type, sep, maxsplit=-1):
    is_true = True if maxsplit <= -1 else False
    string, indexes, output = "", (), []
    sep_len = len(sep)

    i, j = 0, len(text)-1
    if split_type == LEFTSTRIP:
        while i < len(text):
            if sep == text[i: i+sep_len]:
                if 0 < maxsplit or is_true:
                    indexes += (i,)
                    maxsplit -= 1
            i += 1
    else:
        while j > -1:
            if sep == text[j-(sep_len-1): j+1]:
                if 0 < maxsplit or is_true:
                    indexes += (j-(sep_len-1),)
                    maxsplit -= 1
            j -= 1
    idx = 0
    while idx < len(text):
        if idx in indexes:
            output.append(string)
            string = ""
            # Emptying the `string` variable
            # to clear pervious stored strings
            idx += sep_len-1
        else:
            string += text[idx]
        idx += 1
    output.append(string)
    return output


def split(text, sep=None, maxsplit=-1):
    """Returns a list of the words in the string, using sep as the delimiter string.
    sep
        The delimiter according which to split the string.
        None (the default value) means split according to any whitespace,
        and discard empty strings from the result.
    maxsplit
        Maximum number of splits to do.
        -1 (the default value) means no limit.
    """

    # Checks for valid arguments and raises error if not valid
    errorhandler([text, str], [maxsplit, int])
    if sep is not None: errorhandler([sep, str])
    if sep == "":
        raise ValueError("empty separator")

    if sep is None:
        return do_split(text, LEFTSTRIP, maxsplit)
    else:
        return do_argsplit(text, LEFTSTRIP, sep, maxsplit)


def rsplit(text, sep=None, maxsplit=-1):
    """Returns a list of the words in the string, using sep as the delimiter string.
    sep
        The delimiter according which to split the string.
        None (the default value) means split according to any whitespace,
        and discard empty strings from the result.
    maxsplit
        Maximum number of splits to do.
        -1 (the default value) means no limit.
    """

    # Checks for valid arguments and raises error if not valid
    errorhandler([text, str], [maxsplit, int])
    if sep is not None: errorhandler([sep, str])
    if sep == "":
        raise ValueError("empty separator")

    if sep is None:
        return do_split(text, RIGHSTRIP, maxsplit)
    else:
        return do_argsplit(text, RIGHSTRIP, sep, maxsplit)