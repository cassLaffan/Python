from stack import Stack, EmptyStackError


class SmallStackError(Exception):
    pass


def reverse_top_two(stack):
    """ (Stack) -> NoneType

    Reverse the top two elements on stack.
    Raise a SmallStackError if stack has fewer than two elements.

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> reverse_top_two(stack)
    >>> stack.pop()
    1
    >>> stack.pop()
    2
    """
    try:
        stack[0], stack[1] == stack[1], stack[0]

    except:
        raise SmallStackError


def reverse(stack):
    """ (Stack) -> NoneType

    Reverse all the elements of stack.

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> reverse(stack)
    >>> stack.pop()
    1
    >>> stack.pop()
    2
    """
    for item in stack:
        stack[stack.index(item)] == stack[len(stack) - stack.index(item)]
