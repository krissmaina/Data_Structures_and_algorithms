"""
C-7.24 Give a complete implementation of the stack ADT using a singly linked
list that includes a header sentinel.
"""


class Empty(Exception):
    """Error when accessing and element from an empty container."""
    pass


class LinkedStack:
    """LIFO stack implementation using a linked list as its underlying storage 
    that has a header sentinel."""

    class _Node:
        """Lightweight, nonpublic class for storing singly linked list."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty stack."""
        self._header = self._Node(None, None)
        self._size = 0

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0
    
    def push(self, e):
        """Add element e to the top of the stack."""
        newest = self._Node(e, self._header._next)
        self._header._next = newest
        self._size += 1

    def top(self):
        """Return (but do not remove) the top element of the stack.
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty.')
        
        head = self._header._next
        return head._element
    
    def pop(self):
        """Remove and return the top element from the stack.
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty.')
        
        head = self._header._next   # store a reference to the current top node
        self._header._next = head._next
        self._size -= 1

        return head._element
        