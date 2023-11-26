"""Code Fragment 10.8/10.9/10.10: An implementation of a SortedTableMap class."""
from typing import List
from Goodrich.Chapter10.map_base import MapBase


class SortedTableMap(MapBase):
    """Map implementation using a sorted table."""

    # Nonpublic behaviors -------------------------------------------------------------------
    def _find_index(self, k, low, high):
        """Return index of the leftmost item with key greater than or equal to k.

        That is, j will be returned such that...

        * All items of slice table[low:j] have key < k
        * All items of slice table[j:high+1] have key >= k

        :returns: high + 1 if no such item qualifies.
        """
        if high < low:
            return high + 1                                         # No element qualifies
        else:
            mid = (low + high) // 2
            if k == self._table[mid].key:
                return mid                                          # Found exact match
            elif k < self._table[mid].key:
                return self._find_index(k, low, mid - 1)            # Note: may return mid
            else:
                return self._find_index(k, mid + 1, high)           # Answer is right of mid

    # Public behaviors ----------------------------------------------------------------------
    def __init__(self):
        """Create an empty map."""
        self._table: List[MapBase._Item] = []

    def __len__(self):
        """Return the number of items in the map."""
        return len(self._table)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j].key != k:
            raise KeyError(f"Key Error: {repr(k)}")

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting exisitng value if present."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j].key == k:
            self._table[j].value = v                                # Reassign value
        else:
            self._table.insert(j, self._Item(k,v))                  # Adds new item

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j].key != k:
            raise KeyError(f"Key Error: {repr(k)}")
        self._table.pop(j)                                          # Delete item

    def __iter__(self):
        """Generate keys of the map ordered from maximum to minimum."""
        for item in reversed(self._table):
            yield item.key

    def find_min(self):
        """Return (key,value) pair with minimum key (or None if empty)."""
        if len(self._table) > 0:
            return self._table[0].key, self._table[0].value
        else:
            return None

    def find_max(self):
        """Return (key,value) pair with maximum key (or None if empty)."""
        if len(self._table) > 0:
            return self._table[-1].key, self._table[-1].value
        else:
            return None

    def find_ge(self, k):
        """Return (key,value) pair with least key greater than or equal to k."""
        j = self._find_index(k, 0, len(self._table) - 1)        # j's key >= k
        if j < len(self._table):
            return self._table[j].key, self._table[j].value
        else:
            return None

    def find_lt(self, k):
        """Return (key,value) pair with the greatest key strictly less than k."""
        j = self._find_index(k, 0, len(self._table) - 1)        # j's key >= k
        if j > 0:
            return self._table[j-1].key, self._table[j-1].value     # Note use of j-1
        else:
            return None

    def find_le(self, k):
        """Return (key,value) pair with the greatest key less than or equal to k."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if len(self._table) > j >= 0:
            return self._table[j].key, self._table[j].value         # j's key !> k
        else:
            return None

    def find_gt(self, k):
        """Return (key,value) pair with the least key strictly greater than k."""
        j = self._find_index(k, 0, len(self._table) - 1)        # j's key >= 1
        if j < len(self._table) and self._table[j].key == k:
            j += 1                                                  # Advanced past match
        if j < len(self._table):
            return self._table[j].key, self._table[j].value
        else:
            return None

    def find_range(self, start, stop):
        """Iterate all (key,value) pairs such that start <= key < stop.

        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if start is None:
            j = 0
        else:                                                       # Else, find first result
            j = self._find_index(start, 0, len(self._table) - 1)
        while j < len(self._table) and (stop is None or self._table[j].key < stop):
            yield self._table[j].key, self._table[j].value
            j += 1
