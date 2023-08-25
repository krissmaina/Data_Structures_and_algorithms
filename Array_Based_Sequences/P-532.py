import numpy as np


def sum_array(A: list, B: list):
    """Adds two three dimensional numeric datasets componentwise."""
    total = 0
    layer1 = len(A)
    layer2 = len(A[0])
    layer3 = len(A[0][0])

    C = A.copy()

    for i in range(layer1):
        for j in range(layer2):
            for k in range(layer3):
                C[i][j][k] = A[i][j][k] + B[i][j][k]

    return C


listA = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
listB = [[[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

print(sum_array(listA, listB))
# print(np.shape(listB))
