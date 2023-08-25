def sum_matrix(A: list):
    """
    R-5.12
    Describe how the built-in sum function can be combined with Python's
    comprehension syntax to compute the sum of all numbers in an nxn data
    set, represented as a list of lists.
    """

    total = 0

    for row in A:
        total += sum(row)

    return total


mylist = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(sum_matrix(mylist))
