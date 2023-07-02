"""Code Fragment 7.20: Class ``FavoritesListMTF`` implementing the move-to-front heuristic.
This class extends ``FavoritesList`` and overrides methods ``_move_up`` and ``top``."""

from overrides import override
from positional_list import PositionalList
from favorites_list import FavoritesList


class FavoritesListMTF(FavoritesList):
    """List of elements ordered with move-to-front heuristic."""

    # We override _move_up to provide move-to-front semantics.
    @override
    def _move_up(self, p):
        """Move accessed item at Position p to front of list."""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))        # Delete/reinsert.

    # We override top because list is no longer sorted.
    @override
    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")

        # We begin by making a copy of the original list.
        temp = PositionalList()
        for item in self._data:                              # Positional lists support iteration.
            temp.add_last(item)

        # We repeatedly find, report, and remove element with the largest count.
        for j in range(k):
            # Find and report next highest from temp.
            high_pos = temp.first()                         # Underscore is the standard in Python.
            walk = temp.after(high_pos)
            while walk is not None:
                if walk.element().__count__ > high_pos.element().__count__:
                    high_pos = walk
                walk = temp.after(walk)
            # We have found the element with the highest.
            yield high_pos.element().__value__              # Report element to user.
            temp.delete(high_pos)                           # Remove from temp list.
