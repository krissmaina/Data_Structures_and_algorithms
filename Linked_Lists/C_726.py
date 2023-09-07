"""
C-7.26 Implement a method, concatenate(Q2) for the LinkedQueue class that
takes all elements of LinkedQueue Q2 and appends them to the end of the
original queue. The operation should run in O(1) time and should result
in Q2 being an empty queue.
"""


class Empty(Exception):
    """Error when accessing an element from an empty container."""
    pass


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
        
    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0  # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size
    
    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty.')
        
        return self._head._element  # front aligned with head of list
    
    def dequeue(self):
        """Remove and return the first element of the queue (i.e FIFO).
        
        Raise Empty Exception if queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty.')
        
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1

        if self.is_empty():     # special case as queue is empty
            self._tail = None   # removed head had been the tail

        return answer
    
    def enqueue(self, e):
        """Add an element e to the back of the queue."""
        newest = self._Node(e, None)    # node will be new tail node

        if self.is_empty():
            self._head = newest     # special case: previous empty
        else:
            self._tail._next = newest
        
        self._tail = newest     # update reference to tail node
        self._size += 1
        
    def concatenate(self, Q2):
        """Appends all elements of Q2 to self."""
        self._tail._next = Q2._head
        self._tail = Q2._tail
        self._size += Q2._size

        Q2.__init__()


if __name__ == '__main__':
    q1 = LinkedQueue()
    for i in range(10):
        q1.enqueue(i)

    q2 = LinkedQueue()
    for i in range(10, 20):
        q2.enqueue(i)

    q1.concatenate(q2)
    print(f'Size of combined queues: {len(q1)}')
    print(f'Size of q2: {len(q2)}')