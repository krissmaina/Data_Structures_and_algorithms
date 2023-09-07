"""
R-7.5 Implement a function that counts the number of nodes in a circularly
linked list.
"""


def count_nodes(L):
    """Counts the number of nodes in a circularly linked list."""
    head = L.head()
    walk = head

    if not head:    # there are no nodes
        return 0

    count = 0
    while walk.next != head:
        count += 1
        walk = walk.next

    return count + 1    # while loop will finish executing before the last node is counted
