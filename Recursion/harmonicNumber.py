def harmonic_number(n: int):
    """Computes the nth harmonic number recursively."""
    assert n >= 1, 'n must be a positive integer greater or equal to one.'

    if n == 1:
        return 1
    else:
        return (1 / n) + harmonic_number(n-1)
    

print(harmonic_number(3))
