"""
R-6.5 Implement a function that reverses a list of elements by pushing them onto
a stack in one order, and writing them back to the list in reversed order.
"""
from array_stack import *


def reverse(A: list):
    """Reverse the elements of a list using a stack."""
    S = ArrayStack()

    for element in A:
        S.push(element)
    
    for i in range(len(A)):
        A[i] = S.pop()


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse(my_list)

print(f'Reversed list: {my_list}')
