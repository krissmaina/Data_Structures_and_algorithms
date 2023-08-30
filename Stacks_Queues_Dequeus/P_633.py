"""
P-6.33 Give an array-based implementation of a double-ended queue supporting
all of the public behaviors shown in Table 6.4 for the collections.deque
class, including use of the maxlen optional parameter. When a lengthlimited
deque is full, provide semantics similar to the collections.deque
class, whereby a call to insert an element on one end of a deque causes an
element to be lost from the opposite side.
"""


class Empty(Exception):
    """Error when attempting to access and element from an empty container."""
    pass


class Dequeue:
    """A class to mimic the collections.dequeue data structure."""
    DEFAULT_CAPACITY = 10

    def __init__(self, maxlen=None):
        """Create an empty Dequeue."""
        if maxlen:
            self._data = [None] * maxlen
        else:
            self._data = [None] * Dequeue.DEFAULT_CAPACITY

        self._front = 0
        self._size = 0
        self._maxlen = maxlen

    def __len__(self):
        """Return the length of the deque."""
        return self._size
    
    def _is_empty(self):
        """Return True if the deque is empty."""
        return self._size == 0
    
    def __getitem__(self, k: int):
        """Return the value at index k of the deque."""
        if k * -1 > 0:  # index is negative
            k += self._size

        return self._data[(self._front + k) % len(self._data)]
    
    def __setitem__(self, index: int, value):
        """Assigns val to the index k (i.e self[k] = val)."""
        if index * -1 > 0:  # negative index
            index += self._size
        
        if not 0 <= index <= self._size - 1:
            raise IndexError('Index out of range.')
        
        self._data[index + self._front] = value
    
    def appendleft(self, e):
        """Add element e to the front of the deque."""
        if not self._maxlen:    # user did not specify the max length of deque
            if self._size == len(self._data):
                self._resize(2 * len(self._data))
        
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1
        
    def append(self, e):
        """Add element e to the end of the deque."""
        if not self._maxlen:
            if self._size == len(self._data):
                self._resize(2 * len(self._data))

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def popleft(self):
        """Remove and return the first element of the deque.
        
        Raise Empty when deque is empty.
        """
        if self._is_empty():
            raise Empty('Deque is Empty.')
        
        first = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front - 1) % len(self._data)
        self._size -= 1

        return first

    def pop(self):
        """Remove and return the last element of the deque.
        
        Raise Empty when deque is empty.
        """
        if self._is_empty():
            raise Empty('Deque is Empty.')
        
        back = (self._front + self._size - 1) % len(self._data)     # index of the last item
        last = self._data[back]
        self._data[back] = None
        self._size -= 1

        return last
    
    def clear(self):
        """Clears all contents of the deque."""
        if self._maxlen:
            length = self._maxlen
        else:
            length = Dequeue.DEFAULT_CAPACITY

        self._data = [None] * length
        self._front = 0
        self._size = 0

    def rotate(self, k: int):
        """Circularly shift rightwards k steps."""
        if self._is_empty():
            raise Empty('Deque is Empty.')
        
        if 0 < k <= self._size - 1:
            raise Exception(f'k must be in the range(1, {self._size-1})')
        
        old = self._data
        walk = self._front

        for _ in range(self._size):
            self._data[walk + k] = old[walk]
            walk = (walk + 1) % len(old)

    def remove(self, e):
        """Remove the first matching element e.
        
        Raise Error when the deque doesn't have element e."""
        if self._is_empty():
            raise Empty('Deque is Empty.')
        
        found = False
        walk = self._front
        for _ in range(self._size):
            if self._data[walk] == e:
                self._data[walk] = None
                found = True
                break
            walk = (walk + 1) % len(self._data)
        
        if found:
            # shift the elements to the right of the first instance of e leftwards
            j = walk
            for _ in range(walk, self._size):
                self._data[j] = self._data[j+1]
                j = (j + 1) % len(self._data)

            # replace the last value with None
            self._data[j] = None
            self._size -= 1
        else:
            raise ValueError(f'Value {e} was not found')
        
    def count(self, e):
        """Count the number of matches of element e."""
        count_number = 0
        walk = self._front
        for k in range(self._size):
            if self._data[walk] == e:
                count_number += 1
            walk = (walk + 1) % len(self._data)

        return count_number

    def _resize(self, cap):
        """Resizes the array to cap >=  len(self)."""
        old = self._data
        self._data = [None] * cap
        walk = self._front

        # shift elements from old to self._data
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)

        self._front = 0


if __name__ == '__main__':
    D = Dequeue()
    D.append(5)
    D.appendleft(3)
    D.appendleft(6)
    D.append(10)

    print(D[0])     # prints 6
    print(D[-1])    # prints 10
    print()

    D.append(10)

    print(D.count(10))  # prints 2
    print()

    D.remove(5)

    print(D.count(5))   # prints 0
    print()

    D.appendleft(4)
    print(D.popleft())  # prints 4
    print()

    D.append(96)
    print(D.pop())  # prints 96
    print()

    D.clear()
    print(len(D))   # prints 0

    D.append(5)
    D.append(3)
    D.append(45)
    D[2] = 54

    print(D[2])     # prints 54
    