def linear_sum(S: list[float], n: int) -> float:
    """Return the sum of the first n numbers of sequence S"""
    assert int(n) == n, 'n must a positive integer'
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]
    

print(linear_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
