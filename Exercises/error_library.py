"""Runtime Errors."""


def bad_type(item):
    """
    (str) -> TypeError

    Arguement must be a alpha string.

    Attempts to convert a given word or string into an integer.

    >>>bad_type('John')
    Traceback (most recent call last):
        File "<error_library.py>", line 36, in <bad_type>
    TypeError: Can't convert 'int' object to str implicitly

    >>>bad_type('Cassandra')
    Traceback (most recent call last):
        File "<error_library.py>", line 36, in <bad_type>
    TypeError: Can't convert 'int' object to str implicitly


    """

    return int(item)


def bad_name(item):
    """
    (str) -> NameError

    Attempts to return original string.

    >>>bad_name(item)
    Traceback (most recent call last):
        File "<error_library.py>", line 56, in <bad_name>
    builtins.NameError: name 'thing' is not defined

    >>>bad_name(item)
    Traceback (most recent call last):
        File "<error_library.py>", line 56, in <bad_name>
    builtins.NameError: name 'thing' is not defined

    """
    return thing


def bad_attribute(num):
    """
    (int) -> str

    Attempts to make the given integer uppercase.

    >>bad_attribute(4)
    Traceback (most recent call last):
        File "<string>", line 76, in <bad_attribute>
    builtins.AttributeError: 'int' object has no attribute 'upper'

    >>>bad_attribute(88)
    Traceback (most recent call last):
        File "<string>", line 76, in <bad_attribute>
    builtins.AttributeError: 'int' object has no attribute 'upper'

    """
    return num.upper()


def bad_index(randomlist):
    """
    list -> IndexError

    When run, attempts to return randomlist[(len(randomlist)+1)]

    >>>bad_index([3, 5, 22, 7])
    Traceback (most recent call last):
        File "<error_library.py>", line 96, in <bad_index>
    builtins.IndexError: list index out of range

    >>>bad_index(['Applebee', 'John', 'Park', 'Cartman'])
    Traceback (most recent call last):
        File "<error_library.py>", line 96, in <bad_index>
    builtins.IndexError: list index out of range

    """
    return randomlist[(len(randomlist)+1)]


def bad_key(string):
    """
    (str) -> str

    Returns the value associated with the given string.

    >>>bad_key('Joseph')
    Traceback (most recent call last):
        File "<error_library.py>", line 119, in <bad_key>
    builtins.KeyError: 'Joseph'

    >>>bad_key('8')
    Traceback (most recent call last):
        File "<error_library.py>", line 119, in <bad_key>
    builtins.KeyError: '8'


    """
    dicton = {}

    return dicton[string]


def bad_zero(bop):
    """
    (int) -> float

    Returns given integer divided by zero.

    >>>bad_zero(9)
    Traceback (most recent call last):
        File "<error_library.py>", line 139, in <bad_zero>
    builtins.ZeroDivisionError: division by zero

    >>>bad_zero(88)
    Traceback (most recent call last):
        File "<error_library.py>", line 139, in <bad_zero>
    builtins.ZeroDivisionError: division by zero

    """
    return bop/0


def bad_import(string):
    """
    (str) -> Module

    Attempts to import a module named 'Cat'.

    >>>bad_import('Lol')
    Traceback (most recent call last):
        File "<error_library.py>", line 160, in <bad_import>
    builtins.ImportError: No module named 'Cat'

    >>>bad_import('Dog')
    Traceback (most recent call last):
        File "<error_library.py>", line 160, in <bad_import>
    builtins.ImportError: No module named 'Cat'

    """

    import Cat
