class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10   # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        
        Raise Empty excemption if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._data[self._front]
    
    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        
        Raise Empty exeption if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty.')
        
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self.front + 1) % len(self._data)
        self._size -= 1

        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    
    def enqueue(self, e):
        """Add an element to the back of the queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))   # double the array size

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):     # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data    # keep track of existing list
        self._data = [None] * cap   # allocate list with new capacity
        walk = self._front

        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]   # intentionally shift indices
            walk = (1 + walk) % len(old)    # use old size as modulus
        self._front = 0     # front has been realigned
