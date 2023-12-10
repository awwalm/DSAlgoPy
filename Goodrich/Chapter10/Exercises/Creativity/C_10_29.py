"""C-10.29 Repeat Exercise C-10.28 for the ProbeHashMap class."""
from overrides import override
from Goodrich.Chapter10.probe_hashmap import ProbeHashMap


class OptimizedPHM(ProbeHashMap):

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:         # Keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1)  # Number 2^x - 1 is often prime

    @override
    def setdefault(self, k, d):
        try:
            return self[k]
        except KeyError:
            j = self._hash_function(k)
            if self._table[j] is None or self._table[j] is self._AVAIL:
                self._table[j] = self._Item(k,d)
            else: self._table.append(self._Item(k,d))
            self._n += 1
            return d
