"""C-6.18 Show how to use the transfer function, described in Exercise R-6.3, and
two temporary stacks, to replace the contents of a given stack S with those
same elements, but in reversed order."""
from array_stack import *


def reverse_stack(S: ArrayStack):
    """Reverses the elements of a stack."""
    if S.is_empty():
        raise Empty('Stack is empty.')
    
    T = ArrayStack()
    for i in range(len(S)):
        T.push(S.pop())

    return T


if __name__ == '__main__':
    stack_s = ArrayStack()

    for i in range(10):
        stack_s.push(i)

    stack_s_reversed = reverse_stack(stack_s)
    print(stack_s_reversed.top())   # 0 should be the top element
