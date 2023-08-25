import ctypes


class DynamincArray:
    """A Dynamic array class akin to a simplified Python list"""

    def __init__(self) -> None:
        """Create an empty array"""
        self._n = 0     # count actual elements
        self._capacity = 1  # default array capacity
        self._A = None  # low level array

    def __len__(self):
        """Return the number of elements stored in the array"""
        return self._n
    
    def __getitem__(self, k):
        """Return element at index k"""
        if -k > 0:  # if k is negative
            k += self._n    # transform it to its equivalent positive index

        if not 0 <= k <= self._n:
            raise IndexError('invalid index')
        
        return self._A[k]   # retrieve from array
    
    def append(self, obj):
        """Add object to the end of the array."""
        if self._n == self._capacity:   # not enough room
            self._resize(2 * self._capacity)    # so double the capacity

        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):   # non public utility
        """Resize internal array to capacity c."""
        B = self._make_array(self, c)   # new (bigger) array
        for k in range(self._n):    # for each existing value
            B[k] = self._A[k]
        
        self._A = B     # use the bigger array
        self._capacity = c

    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()
    
    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # for simplicity, we assume 0 <= k <= n in this version.
        if self._n == self._capacity:   # not enough room
            # self._resize(2 * self._capacity)    # so double the capacity
            B = self._make_array(2 * self._capacity)

            for j in range(self._n + 1):
                if j < k:   # values before k remains at the same index
                    B[j] = self._A[j]
                elif j == k:    # insert the new value at index k
                    B[j] = value
                elif j > k:     # shift the rest of the values rightmost
                    B[j] = self._A[j-1]

            self._A = B
            self._n += 1
            return
            
        for j in range(self._n, k, -1):     # shift rightmost first
            self._A[j] = self._A[j-1]

        self._A[k] = value  # store the newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurence of value (or raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version.
        for k in range(self._n):
            if self._A[k] == value:     # found a match

                for j in range(k, self._n):     # shift others to fill the gap
                    self._A[j] = self._A[j+1]

                self._A[self._n-1] = None   # help garbage collection
                self._n -= 1    # we have one less item

                return  # exit immediately
        raise ValueError('value not found')     # only reached if no match
    
    def pop(self, element):
        """Removes the last element of the DynamicArray."""
        # grab the last element
        lst_element = self._A[self._n-1]

        self._A[self._n-1] = None
        self._n -= 1

        if self._n < (self._capacity // 4) + 1:
            self._resize(self._capacity // 2)
            
        return lst_element