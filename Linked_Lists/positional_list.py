from doubly_linked_base import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    # --------------------- nested Positional class -----------------
    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element
        
        def __eq__(self, other):
            """Return True if other is a position representing the same location."""
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)  # opposite of __eq__
        
    # ----------------------utility method -----------------------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type.')
        
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        
        if p._node._next is None:   # convection for deprecated node
            raise ValueError('p is no longer valid.')
        
        return p._node
    
    # ---------------------utility method -------------------------------
    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None     # boundary violation
        else:
            return self.Position(self, node)    # legitimate position
        
    # -----------------------------accessors ------------------------------
    def first(self):
        """Return the first Position in the list(or None if the list is empty)."""
        return self._make_position(self._header._next)
    
    def last(self):
        """Return the last Position in the list (or None id the list is empty)."""
        return self._make_position(self._trailer._prev)
    
    def before(self, p: Position):
        """Return the Position just before Position p (or None if p is the first)."""
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p: Position):
        """Return the Postion just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()

        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # --------------------------- mutators --------------------------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add and element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer_prev, self._trailer)
    
    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    
    def add_after(self, p, e):
        """Insert element e into list after Positon p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete(self, p):
        """Remove and return the element at Positon p."""
        original = self._validate(p)
        return self._delete_node(original)  # inherited method returns element
    
    def replace(self, p, e):
        """Replace the element at Position p with e.
        
        Return the element formely at Positon P.
        """
        original = self._validate(p)
        old_value = original._element   # temporarily store old element
        original._element = e   # replace with new element
        return old_value    # return the old element value


def insertion_sort(L: PositionalList):
    """Sort PositionalList of comparable elements into nondecreasing order."""
    if len(L) > 1:  # otherwise, no need to sort it
        marker = L.first()

        while marker != L.last():
            pivot = L.after(marker)     # next item to place
            value = pivot.element()

            if value > marker.element():    # pivot is already sorted
                marker = pivot  # pivot becomes new marker
            else:   # must relocate pivot
                walk = marker   # find leftmost item greater than value

                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)

                L.delete(pivot)
                L.add_before(walk, value)   # reinsert value before walk
                