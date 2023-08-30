from array_stack import *


def is_matched(expr):
    """Return True if all delimeters are properly matched; False otherwise."""
    lefty = '({['   # opening delimeters
    righty = ')}]'  # respective closing delimeters

    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)   # push left delimeter on stack
        elif c in righty:
            if S.is_empty():
                return False    # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                return False    # mismatched
    return S.is_empty()     # were all symbols matched?


print(is_matched('[(5+x) - (y+z)]'))
