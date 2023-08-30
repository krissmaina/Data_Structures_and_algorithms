"""
P-6.34 Implement a program that can input an expression in postfix notation (see
Exercise C-6.22) and output its value.
"""
from array_stack import *


def evaluate_postfix(expr: str):
    """Evaluates and returns the value in the postfix notation.
    Assuming a valid postfix notation is inputted.
    """
    S = ArrayStack()
    value = ""

    for char in expr:
        if char.isnumeric():
            S.push(int(char))
        elif char in ['+', '-', '*', '/']:
            val = None
            val2, val1 = S.pop(), S.pop()   # pop the last 2 items
            val = eval(f'{val1} {char} {val2}')

            S.push(val)

    return S.pop()


if __name__ == '__main__':
    print(evaluate_postfix('5 2 + 8 3 - * 4 /')) # prints 8.75
