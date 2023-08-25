def sum_numbers(A: list):
    """Computes sum of all numbers in a n x n data set."""
    total = 0

    for row in A:
        for column in row:
            total += column
    
    return total


mylist = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(sum_numbers(mylist))
