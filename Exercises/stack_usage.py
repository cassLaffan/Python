from stack import Stack


def remove_second(stack):
    """ (Stack) -> object

    Remove and return the second-highest item on stack.
    You may assume that stack always has at least two items.

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(10)
    >>> stack.push(30)
    >>> stack.push(40)
    >>> remove_second(stack)
    30 # Second most recent element added
    >>> stack.pop()
    40 # Top element remains unchanged
    >>> stack.pop()
    10 # Next element is now 10; the 30 has been removed
    >>> stack.pop()
    1
    >>> stack.is_empty()
    True
    """

    while stack.is_empty() == False:
        stack.pop(1)
