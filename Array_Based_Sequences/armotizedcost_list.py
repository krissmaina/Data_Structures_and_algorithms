from time import time


def compute_average(n):
    """Perform n appends to a list and return the average time elapsed."""
    data = []
    start = time()

    for k in range(n):
        data.append(None)
    
    end = time()

    return (end - start) / n

print(compute_average(1_000_000))
