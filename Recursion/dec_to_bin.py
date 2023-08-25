# def decimal_to_binary(n: int):
#     """Transforms a decimal to binary recursively."""

#     assert int(n) == n, 'n must be an integer.'
#     rem = n % 2

#     quotient = n // 2

#     if quotient == 0:
#         return str(rem)
#     else:
#         return decimal_to_binary(quotient) + str(rem)
    

# print(decimal_to_binary(-2))
# print(bin(2))

def dec_to_bin(n: int):
    """Transforms a decimal to binary recursively."""
    assert int(n) == n, 'n must an integer'

    if n == 0:  # if the quotient is equal to zero
        return 0
    else:
        return n % 2 + 10 * dec_to_bin(int(n / 2))
    

print(dec_to_bin(-13))
