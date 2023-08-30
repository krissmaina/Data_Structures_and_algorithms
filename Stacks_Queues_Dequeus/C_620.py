"""
C-6.20 Describe a nonrecursive algorithm for enumerating all permutations of the
numbers {1,2, . . . ,n} using an explicit stack.
"""

from array_stack import *


def permutations(n):
  # Initialize an empty stack S and a list P to store the permutations
  S = ArrayStack()
  P = []
  # Push an empty list to S
  S.push([])
  # While S is not empty, do the following
  while S:
    # Pop the top list from S and store it in a variable L
    L = S.pop()
    # If L has length n, then append L to P
    if len(L) == n:
      P.append(L)
    # Else, for each number i from 1 to n that is not in L, do the following
    else:
      for i in range(1, n + 1):
        if i not in L:
          # Create a new list M by appending i to L
          M = L + [i]
          # Push M to S
          S.push(M)
  # Return P as the final list of permutations
  return P


perm = permutations(4)

for p in perm:
  print(p)
