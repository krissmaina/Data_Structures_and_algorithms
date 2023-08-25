def sumofDigits(n):
    """Recursive approach to find the sum of digits of a positive integer"""
    assert n >= 0 and int(n) == n, "n must be a positive integer."
    if len(str(n)) == 1:
        return n
    else:
        return n % 10 + sumofDigits(n // 10)


print(sumofDigits(-1))

# def sum_of_digits(n):
#     """Iterative approach to find the sum of digits of a positive integer."""
#     n = str(n)

#     total = 0
#     for i in n:
#         j = int(i)
#         total += j

#     return total


# print(sum_of_digits(1111))
