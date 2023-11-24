"""Code Fragment 10.5: Concrete hash map class with separate chaining."""

from Goodrich.Chapter10.hashmap_base import HashMapBase
from Goodrich.Chapter10.unsorted_table_map import UnsortedTableMap


class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError(f"Key Error: {repr(k)}")         # No match found
        return bucket[k]                                    # May rause KeyError

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()             # Bucket is new to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:                   # Key was new to the table
            self._n += 1                                    # Increase overal map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError(f"Key Error: {repr(k)}")         # No match found
        del bucket[k]                                       # May raise KeyError

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:                          # A nonempty slot
                for key in bucket:
                    yield key

