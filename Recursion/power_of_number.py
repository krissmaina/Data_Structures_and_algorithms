# def power(base, exp):
#     """
#     Calculates the power of the base with the exponent recursively.
#     Returns base ^ exp
#     """
#     assert exp >= 0 and int(exp) == exp , 'the exponent must be an integer greater than zero.'
#     if exp == 0:
#         return 1
#     else:
#         return base * power(base, exp - 1)
    

# print(power(-3.2, 2))


def power(x, n: int) -> float:
    """Compute the value of x**n for integer n"""
    assert int(n) == n, 'n must be a positive integer'

    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)  # rely on truncated division
        result = partial * partial

        if n % 2 == 1:  # if n is odd, include an extra factor of x
            result *= x
        
        return result
    

print(power(2, 1))
