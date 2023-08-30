"""
R-6.3 Implement a function with signature transfer(S, T) that transfers all elements
from stack S onto stack T, so that the element that starts at the top
of S is the first to be inserted onto T, and the element at the bottom of S
ends up at the top of T.
"""
from array_stack import *


def transfer(S: ArrayStack, T: ArrayStack):
    """Transfers all elements from stack S onto stack T, 
    so that the elements that start at he top of S is the first to be inserted onto T,
    and the element at the bottom of S ends up at the top of T."""
    if S.is_empty():
        raise Empty('Stack S is empty.')

    for i in range(len(S)):
        top = S.pop()
        T.push(top)


stack_s = ArrayStack()
for i in range(10):
    stack_s.push(i)

print(stack_s)

stack_t = ArrayStack()
print('\n\nTransferring elements from stack S to stack T.')
transfer(stack_s, stack_t)
print()
print(stack_t)
