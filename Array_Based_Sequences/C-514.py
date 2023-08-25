from random import randrange


def shuffle_list(A: list) -> list:
    """Re-arranges the list so that every possible ordering is likely."""
    n = len(A)

    B = []
    while True:
        rand_num = randrange(n)

        if rand_num in B:
            continue

        B.append(rand_num)

        if len(B) == n:
            break

    C = [A[i] for i in B]

    return C


def my_shuffle(lst):
    """Efficient way to shuffle a list."""
    # get the length of the list
    n = len(lst)

    # loop through the list indices
    for i in range(n):
        # generate a random index between i and n-1
        j = randrange(i, n)
        # swap the elements at i and j
        lst[i], lst[j] = lst[j], lst[i]
        
    # return the shuffled list
    return lst


print(shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
