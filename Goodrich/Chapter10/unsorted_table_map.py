"""Code Fragment 10.3: An implementation of a map using a Python list as an unsorted table."""
from typing import List
from Goodrich.Chapter10.map_base import MapBase


# noinspection PyProtectedMember
class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        """Create an empty map."""
        self._table: List[MapBase._Item] = []                            # List of _Items

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError(repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._Item(k,v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError(repr(k))

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key

