"""Code Fragment 10.4:
A base class for our hash table implementations, extending our MapBase class from Code Fragment 10.2."""
from random import randrange
from typing import Union, List

from Goodrich.Chapter10.map_base import MapBase
from Goodrich.Chapter10.unsorted_table_map import UnsortedTableMap


# noinspection PyAbstractClass
class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map."""
        self._table: List[Union[                    # Lookup table/bucket array
            MapBase._Item,                          # Direct storage for linear probing
            List,                                   # Independent bucket for separate chaining
            UnsortedTableMap,                       # Alternate bucket type for separate chaining
            object,                                 # For indicating available space
            None
        ]] = cap * [None]
        self._n = 0                                 # Number of entries in the map
        self._prime = p                             # Prime for MAD compression
        self._scale = 1 + randrange(p-1)            # Scale from 1 to p-1 for MAD
        self._shift = randrange(p)                  # Shift from 0 to p-1 for MAD

    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    # noinspection PyUnresolvedReferences
    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)           # Abstract method; May raise KeyError

    # noinspection PyUnresolvedReferences
    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)               # Abstract method; Subroutine maintains self._n
        if self._n > len(self._table) // 2:         # Keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1)  # Number 2^x - 1 is often prime

    # noinspection PyUnresolvedReferences
    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)                  # Abstract method; May raise KeyError
        self._n -= 1

    def _resize(self, c):                           # Resuze bucket array to capacity c
        old = list(self.items())                    # Use iteration to record existing items
        self._table = c * [None]                    # Then reset table to desired capacity
        self._n = 0                                 # n recomputed during subsequent adds
        for (k,v) in old:
            self[k] = v                             # Reinsert old key-value pair
