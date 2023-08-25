def fibonnaci(n):
    assert n >= 0 and int(n) == n, "Fibonacci number cannot be negative number or non integer."
    if n in [0, 1]:
        return n
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)


print(fibonnaci(-1))
