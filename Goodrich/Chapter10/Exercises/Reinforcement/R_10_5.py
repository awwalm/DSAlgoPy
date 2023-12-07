"""R-10.5 Reimplement the UnsortedTableMap class from Section 10.1.5,
using the PositionalList class from Section 7.4 rather than a Python list."""

from __future__ import annotations
from Goodrich.Chapter7.positional_list import PositionalList

class UnsortedTableMap:
    """TAKE CAUTION:\n
    * PositionalList stores _Node objects (NOT Positions).
    * Iterating through PositionalList yields explicit abitaririly typed objects (NOT Positions).
    """

    class _Item:
        """Lightweight composite to store key-value pairs as map items."""
        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other: UnsortedTableMap._Item):
            return self._key == other._key          # Compare items based on their keys

        def __ne__(self, other: UnsortedTableMap._Item):
            return not (self == other)              # Opposite of __eq__

        def __lt__(self, other: UnsortedTableMap._Item):
            return self._key < other._key           # Compare items based on their keys

        @property
        def key(self):
            return self._key

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self._value = value

    def __init__(self):
        self._table = PositionalList()

    def __getitem__(self, k):
        for element in self._table:
            if k == element.key:
                return element.value
        raise KeyError(k)

    def __setitem__(self, k, v):
        if len(self._table) == 0:
            self._table.add_first(self._Item(k,v))
            return
        for element in self._table:
            if k == element.key:
                element.value = v
                return
        self._table.add_last(self._Item(k,v))

    def __delitem__(self, k):
        cur = self._table.first()
        while cur is not None:
            if cur.element().key == k:
                self._table.delete(cur)
                return
            cur = self._table.after(cur)
        raise KeyError(repr(k))

    def __iter__(self):
        return self._table.__iter__()

    def __len__(self):
        return len(self._table)

    def __str__(self):
        return "{" + ", ".join([f"{i}: {j.value}" for i,j in zip(self.keys(), self.items())]) + "}"

    def items(self):
        for element in self._table:
            yield element

    def keys(self):
        for element in self._table:
            yield element.key
