from positional_list import PositionalList
from favorite_list import FavoritesList


class FavoritesListMTF(FavoritesList):
    """List of elements ordered with move-to-front heuristic."""

    # we override _move_up to provide move-to-front semantics
    def _move_up(self, p):
        """Move accessed item at Position p to front of list."""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))  # delete/reinsert

    # we override top because list is no longer sorted
    def top(self, k: int):
        """Genereate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k.')
        
        # we begin by making a copy of the original list
        temp = PositionalList()
        for item in self._data:     # positional lists support iteration
            temp.add_last(item)

        # we repeatedly find, report, and remove element with largest count
        for j in range(k):
            # find and report next higherst from temp
            highPos = temp.first()
            walk = temp.after(highPos)

            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            
            # we found the element with the highest count
            yield highPos.element()._value  # report element to user
            temp.delete(highPos)    # remove from temp list