def gcd(a: int, b: int) -> int:
    """Finds the greatest common divisor of two positive integers using recursion."""
    assert int(a) == a and int(b) == b, "a and b must be integers."

    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b

    rem = a % b
    if rem == 0:
        return b
    else:
        return gcd(b, rem)


print(gcd(48, -18))
