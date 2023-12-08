"""R-10.15 Our HashMapBase class maintains a load factor λ ≤ 0.5.
Reimplement that class to allow the user to specify the maximum load,
and adjust the concrete subclasses accordingly."""
# @TODO: Adjusting the concrete subclasses is trivial so, not doing it for now.
from Goodrich.Chapter10.hashmap_base import HashMapBase

# noinspection PyAbstractClass
class DynamicLoadHashMapBase(HashMapBase):

    def __init__(self, cap, p, load: float):
        super().__init__(cap=cap, p=p)
        self._load = load

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)                   # Abstract method; Subroutine maintains self._n
        if (self._n/len(self._table)) > self._load:     # Keep load factor <= self._load
            self._resize(2 * len(self._table) - 1)      # Number 2^x - 1 is often prime

    def _bucket_setitem(self, j, k, v):
        raise NotImplementedError
