"""Code Fragment 7.18/.19: Class ``FavoritesList``."""
from positional_list import PositionalList


class FavoritesList:
    """List of elements ordered from most frequently accessed to least."""

    # Nested _Item class -------------------------------------------------------------------
    class _Item:
        __slots__ = "_value", "_count"                      # Streamline memory usage.

        def __init__(self, e):
            self._value = e                                 # The user's element.
            self._count = 0                                 # Access count initially zero.

        @property
        def __value__(self):
            return self._value

        @property
        def __count__(self):
            return self._count

        @__count__.setter
        def __count__(self, value):
            self._count = value

    # Nonpublic utilities ------------------------------------------------------------------
    def _find_position(self, e):
        """Search for element e and return its ``Position`` (or ``None`` if not found)."""
        walk = self._data.first()
        while walk is not None and walk.element().__value__ != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p: PositionalList.Position):
        """Move item at ``Position`` p earlier in the list based on access count."""
        if p != self._data.first():                         # Consider moving...
            cnt = p.element().__count__
            walk = self._data.before(p)
            if cnt > walk.element().__count__:              # Must shift forward.
                while walk != self._data.first() and cnt > self._data.before(walk).element().__count__:
                    walk = self._data.before(walk)
                self._data.add_before(
                    walk, self._data.delete(p))             # Delete/reinsert.

    # Public methods -----------------------------------------------------------------------
    def __init__(self):
        self._data = PositionalList()                       # Will be list of _Item instances.

    def __len__(self):
        """Return number of entries on favorites list."""
        return len(self._data)

    def is_empty(self):
        """Return ``True`` if list is empty."""
        return len(self._data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count."""
        p = self._find_position(e)                          # Try to locate existing element.
        if p is None:
            p = self._data.add_last(self._Item(e))          # If new, place at end.
        p.element().__count__ += 1                          # Always increment count.
        self._move_up(p)                                    # Consider mmoving forward.

    def remove(self, e):
        """Remove element e from the list of favorites."""
        p = self._find_position(e)                          # Try to locate existing element.
        if p is not None:
            self._data.delete(p)                            # Delete, if found.

    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError(f"Illegal value for k = {k}")
        walk = self._data.first()
        for j in range(k):
            item = walk.element()                           # Element of list is _Item.
            yield item.__value__                            # Report user's element.
            walk = self._data.after(walk)
