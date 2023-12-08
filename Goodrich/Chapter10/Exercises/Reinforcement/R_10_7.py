"""R-10.7 Our Position classes for lists and trees support the eq method so that two distinct
position instances are considered equivalent if they refer to the same underlying node in a structure.
For positions to be allowed as keys in a hash table, there must be a definition for the hash method
that is consistent with this notion of equivalence. Provide such a hash method."""
# @FIXME: It makes no sense to use a "Position" as key (how do you query __getitem__ ?) but here's the code anyway:
from random import randrange
from Goodrich.Chapter7.positional_list import PositionalList

class PositionalHashMap(PositionalList):

    class HashPosition(PositionalList.Position):
        def __init__(self, container, node):
            super(PositionalHashMap.HashPosition, self).__init__(container, node)
            self._prime = 109345121
            self._scale = 1 + randrange(self._prime-1)
            self._shift = randrange(self._prime)
            self._table = []

        def __hash__(self):
            return (
                (hash(self.node.element) * self._scale      # MULTIPLY
                + self._shift)                              # ADD
                % self._prime % len(self.container)         # DIVIDE
            )

        def __eq__(self, other):
            if super().__eq__(other):
                return self.__hash__() == other.__hash__()

        def __getitem__(self, item):
            """Refer to the `Java-style documentation of the inbuilt LinkedHashMap class
            <https://docs.oracle.com/javase/8/docs/api/java/util/LinkedHashMap.html>`.
            It specifies the dual maintainance structure of both a lookup table for each key-value item,
            and a corresponding linked list."""
            raise NotImplementedError

        def __setitem__(self, key, value):
            __doc__ = self.__getitem__.__doc__
            raise NotImplementedError
