"""
C-6.22 Postfix notation is an unambiguous way of writing an arithmetic expression
without parentheses. It is defined so that if “(exp1)op(exp2)” is a
normal, fully parenthesized expression whose operation is op, the postfix
version of this is “pexp1 pexp2 op”, where pexp1 is the postfix version of
exp1 and pexp2 is the postfix version of exp2. The postfix version of a single
number or variable is just that number or variable. For example, the
postfix version of “((5+2) * (8-3))/4” is “5 2 + 8 3 - * 4 /”. Describe
a nonrecursive way of evaluating an expression in postfix notation.
"""
from array_stack import *


def postfix_notation(expr: str) -> str:
    """Writing an arithmetic expression in an unambiguous way (postfix notation)."""
    S = ArrayStack()
    output = []

    for char in expr:
        if char.isnumeric():
            output += char
        elif char == '(':
            S.push(char)
        elif char == ')':

            while S:
                popped = S.pop()
                if popped in ['+', '-', '*', '/']:
                    output += popped
                elif popped == '(':
                    break
        elif char in ['+', '-', '*', '/']:
            S.push(char)

    while S:
        op = S.pop()
        if op in ['+', '-', '*', '/']:
            output += op
    
    return " ".join(output)


print(postfix_notation('((5+2) * (8 - 3)) / 4'))
