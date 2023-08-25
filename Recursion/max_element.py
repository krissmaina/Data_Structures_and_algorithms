def maximum(S: list[int], n: int) -> int:
    """Finds the maximum element of a sequence S recursively."""
    assert n >= 0, 'n must be a positive integer.'

    if n == 0:  # no elements in the sequence
        return 0
    elif n == 1:    # only one element in the sequence
        return S[n-1]
    else:   # if there are 2 or more elements in the sequence
        result = maximum(S[:n-1], n-1)
        if S[n-1] > result:
            return S[n-1]
        else:
            return result


print(maximum([56, 2, 3, 4, 7, 14], 6))
