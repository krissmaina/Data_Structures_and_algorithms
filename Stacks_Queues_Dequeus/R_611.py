"""
R-6.11 Give a simple adapter that implements our queue ADT while using a
collections.deque instance for storage.
"""
from collections import deque


class Empty(Exception):
    """Error accessing element from an empty container."""
    pass


class ArrayQueue:
    """FIFO queue implementation using deque as its underlying storage."""

    def __init__(self):
        """Create an empty queue."""
        self._data = deque()

    def __len__(self):
        """Return the length of the queue."""
        return len(self._data)
    
    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self._data) == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._data[0]
    
    def dequeue(self):
        """Remove and return the first element of the queue (i.e, FIFO).
        
        Raise Empty exeption if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._data.popleft()
    
    def enqueue(self, e):
        """Add an element to the back of the queue."""
        self._data.append(e)


if __name__ == '__main__':
    queue = ArrayQueue()
    queue.enqueue(5)
    queue.enqueue(3)
    queue.dequeue()
    queue.enqueue(8)
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(9)
    queue.enqueue(1)
    queue.dequeue()
    queue.enqueue(7)
    queue.enqueue(6)
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(4)
    queue.dequeue()
    queue.dequeue()
    
    print(f'queue has {len(queue)} elements.')  # len should be zero
    