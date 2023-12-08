"""C-10.29 Repeat Exercise C-10.28 for the ProbeHashMap class."""
from overrides import override
from Goodrich.Chapter10.probe_hashmap import ProbeHashMap


class OptimizedPHM(ProbeHashMap):

    def __getitem__(self, k):
        query = self._find_slot(0, k)
        if query[0]:
            return self._table[query[1]].value
        raise KeyError

    def __setitem__(self, k, v):
        return self._bucket_setitem(0, k, v)

    @override
    def setdefault(self, k, d):
        try:
            return self[k]
        except KeyError:
            if self._table[-1] is self._AVAIL:
                self._table[-1] = self._Item(k,d)
            else: self._table.append(self._Item(k,d))
            return d
