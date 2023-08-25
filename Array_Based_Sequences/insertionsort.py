def insertion_sort(A: list[float | int]) -> list[float | int]:
    """Sort list of comparable items into non decreasing order."""
    for k in range(1, len(A)):  # from 1 to n-1
        cur = A[k]  # current element to be inserted
        j = k   # find correct index j for current

        while j > 0 and A[j-1] > cur:   # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1

        A[j] = cur  # cur is now at the right place
        