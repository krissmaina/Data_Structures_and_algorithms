class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class Full(Exception):
    """Error attempting to add an element when the container is full."""
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self, maxlen: int = None):
        """Create an empty stack."""
        self._data = [] * maxlen     # nonpublic list instance
        self._maxlen = maxlen

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0
    
    def push(self, e):
        """Add element e to the top of the stack."""
        if len(self) == self._maxlen:
            raise Full('Stack is already full, cannot add an element.')
        self._data.append(e)    # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data[-1]   # the last item in the list
    
    def pop(self):
        """Remove and return the element from the top of the stack. (i.e LIFO).
        
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data.pop()     # remove the last item from the list
    

if __name__ == '__main__':
    S = ArrayStack(10)

    for i in range(12):
        S.push(i)
