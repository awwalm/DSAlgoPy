"""C-10.30 Repeat Exercise C-10.28 for the ChainHashMap class."""
from overrides import override
from Goodrich.Chapter10.chain_hashmap import ChainHashMap


class OptimizedCHM(ChainHashMap):

    def __getitem__(self, k):                       # Total runtime: O(λ) = O(n/N) ~ O(1)
        j = self._hash_function(k)                  # Obtain corresponding hashed index j in lookup table T
        return self._bucket_getitem(j, k)           # Find M[k] located in map/bucket M stored in index j of T

    def __setitem__(self, k, v):
        j = self._hash_function(k)                  # Obtain provisional hashed index j to be used in lookup table T
        self._bucket_setitem(j, k, v)               # Insert v into map/bucket at index j of T, identified by key k
        if self._n > len(self._table) // 2:         # Keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1)  # Number 2^x - 1 is often prime

    @override
    def setdefault(self, k, d):
        try:
            return self[k]
        except KeyError:
            self[k] = d
            return d
