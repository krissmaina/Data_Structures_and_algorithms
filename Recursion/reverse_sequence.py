def reverse(S: list, start: int, stop: int) -> None:
    """Reverse elements in implicit slice S[start: stop]"""
    if start < stop - 1:    # if at least two elements
        S[start], S[stop-1] = S[stop-1], S[start]   # swap the first and last item
        reverse(S, start+1, stop-1)     # recur on the rest
        