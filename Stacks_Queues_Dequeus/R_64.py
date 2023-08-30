"""
R-6.4 Give a recursive method for removing all the elements from a stack.
"""
from array_stack import *


def clear(S: ArrayStack):
    """Recursive way for removing all elements from a Stack."""
    if S.is_empty():
        return
    S.pop()
    clear(S)


stack_s = ArrayStack()
for i in range(10):
    stack_s.push(i)

print(f'Is stack s empty: {stack_s.is_empty()}')

clear(stack_s)

print(f'After clear function, is stack s empty: {stack_s.is_empty()}')
