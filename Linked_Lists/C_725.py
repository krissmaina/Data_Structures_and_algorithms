"""
C-7.25 Give a complete implementation of the queue ADT using a singly linked
list that includes a header sentinel.
"""


class Empty(Exception):
    """Error when accessing and element from an empty container."""
    pass


class LinkedQueue:
    """FIFO Queue implementation using a singly linked list 
    that includes a header sentinel."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked list."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty queue."""
        self._header = self._Node(None, None)
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size
    
    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the top element of the queue.
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty.')
        
        head = self._header._next
        return head._element
    
    def dequeue(self):
        """Return and remove the top element of the queue.
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty.')
        
        head = self._header._next
        self._header._next = head._next
        self._size -= 1

        return head._element
    
    def enqueue(self, e):
        """Add element e to the back of the queue."""
        newest = self._Node(e, None)

        if self.is_empty():
            self._tail = newest
            self._header._next = self._tail
        else:
            self._tail._next = newest
            self._tail = newest
        
        self._size += 1


if __name__ == '__main__':
    q = LinkedQueue()

    for i in range(10):
        q.enqueue(i)

    print(len(q))   # prints 10

    while q:
        print(f'First: {q.first()}', end=" ")
        print(f'Length: {len(q)}')

        q.dequeue()
