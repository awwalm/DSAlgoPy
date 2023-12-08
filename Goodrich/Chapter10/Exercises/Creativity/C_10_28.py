"""C-10.28 On page 406 of Section 10.1.3, we give an implementation of the
method setdefault as it might appear in the MutableMapping abstract base class.
While that method accomplishes the goal in a general fashion, its efficiency is less than ideal.
In particular, when the key is new, there will be a failed search due to the initial use of getitem ,
and then a subsequent insertion via setitem . For a concrete implementation, such as the UnsortedTableMap,
this is twice the work because a complete scan of the table will take place during the failed getitem ,
and then another complete scan of the table takes place due to the implementation of setitem .
A better solution is for the UnsortedTableMap class to override setdefault to provide a direct solution
that performs a single search. Give such an implementation of UnsortedTableMap.setdefault."""
from overrides import override
from Goodrich.Chapter10.unsorted_table_map import UnsortedTableMap


class OptimizedUTM(UnsortedTableMap):
    @override
    def setdefault(self, k, d):
        try:
            return self[k]
        except KeyError:
            self._table.append(self._Item(k,d))
            return d
