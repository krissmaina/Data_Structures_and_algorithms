"""
P-6.35 The introduction of Section 6.1 notes that stacks are often used to provide
“undo” support in applications like a Web browser or text editor. While
support for undo can be implemented with an unbounded stack, many
applications provide only limited support for such an undo history, with a
fixed-capacity stack. When push is invoked with the stack at full capacity,
rather than throwing a Full exception (as described in Exercise C-6.16),
a more typical semantic is to accept the pushed element at the top while
“leaking” the oldest element from the bottom of the stack to make room.
Give an implementation of such a LeakyStack abstraction, using a circular
array with appropriate storage capacity. This class should have a public
interface similar to the bounded-capacity stack in Exercise C-6.16, but
with the desired leaky semantics when full.
"""
class Empty(Exception):
    """Error when accessing and element from an empty container."""
    pass


class LeakyStack:
    """LIFO Stack implementation with fixed amount of storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty stack."""
        self._data = [None] * LeakyStack.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        """Return the length of the Stack."""
        return self._size
    
    def is_empty(self):
        """Return True if the Stack is empty."""
        return self._size == 0
    
    def push(self, e):
        """Add element e to the top of the Stack."""
        self._front = (self._front + 1) % len(self._data)

        self._data[self._front] = e

        if not self._size == len(self._data):
            self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise Empty if the Stack is empty."""
        if self.is_empty():
            raise Empty('Stack is Empty.')
        
        return self._data[self._front]
    
    def pop(self):
        """Remove and return the top element at the Stack.
        
        Raise Empty if the Stack is empty."""
        if self.is_empty():
            raise Empty('Stack is Empty.')
        
        item = self._data[self._front]
        self._front = (self._front - 1) % len(self._data)
        self._size -= 1

        return item
    

if __name__ == '__main__':
    L = LeakyStack()

    for i in range(15):
        L.push(i)

    print(len(L))   # prints 10

    L.pop()

    print(len(L))   # prints 9
    print(L.top())  # prints 13
