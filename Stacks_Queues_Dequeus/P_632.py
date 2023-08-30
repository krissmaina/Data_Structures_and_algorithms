"""
P-6.32 Give a complete ArrayDeque implementation of the double-ended queue
ADT as sketched in Section 6.3.2.
"""


class Empty(Exception):
    """Error when accessing an element from an empty container."""
    pass


class ArrayDequeue:
    """A class to represent Double-Ended Queues."""
    DEFAULT_CAPACITY = 10   # moderate capacity of all new dequeues

    def __init__(self):
        """Create and empty deque."""
        self._data = [None] * ArrayDequeue.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        """Return the size of the dequeue."""
        return self._size
    
    def is_empty(self):
        """Return True if the dequeue is empty."""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the first element in the dequeue.
        
        Raise Empty if the dequeue is empty.
        """
        if self.is_empty():
            raise Empty('Dequeue is Empty.')
        
        return self._data[self._front]
    
    def last(self):
        """Return (but do not remove) the last element in the Dequeue.
        
        Raise Empty if the dequeue is empty.
        """
        back = (self._size + self._front - 1) % len(self._data)     # index of the last element
        return self._data[back]
    
    def add_first(self, e):
        """Add element e to the front of the Dequeue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))   # double the array size

        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        """Add element e to the back of the Dequeue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        avail = (self._size + self._front) % len(self._data)

        self._data[avail] = e
        self._size += 1

    def delete_first(self):
        """Remove and return the first element from the Dequeue.
        
        Raise Empty if the dequeue is empty.
        """
        if self.is_empty():
            raise Empty('Dequeue is Empty.')
        
        first = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        return first
    
    def delete_last(self):
        """Remove and return the last element from the Dequeue.
        
        Raise Empty if the dequeue is empty.
        """
        if self.is_empty():
            raise Empty('Dequeue is Empty.')
        
        back = (self._size + self._front - 1) % len(self._data)     # index of the last item
        last = self._data[back]
        self._data[back] = None
        self._size -= 1

        return last
    
    def _resize(self, cap: int):
        """Resize a new list of capacity >= len(self)."""
        old = self._data
        self._data = [None] * cap
        walk = self._front

        # shifting the elements in old to the self._data
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)

        self._front = 0 

        
if __name__ == '__main__':
    D = ArrayDequeue()
    D.add_first(5)
    D.add_last(3)
    
    print(D.first())    # prints 5
    print(D.last())     # prints 3
    print()

    D.add_first(2)
    D.add_first(8)
    D.add_last(1)
    D.add_last(6)

    print(D.first())    # prints 8
    print(D.last())     # prints 6
    print()

    D.delete_first()
    D.delete_first()

    print(D.first())    # prints 5
    print()

    i = D.delete_last()
    print(i)    # prints 6
