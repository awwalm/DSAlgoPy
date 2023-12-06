"""R-10.2 Give a concrete implementation of the items() method in the context of the MutableMapping class,
relying only on the five primary abstract methods of that class.
What would its running time be if directly applied to the UnsortedTableMap subclass?"""

from collections.abc import MutableMapping


# noinspection PyPep8Naming
class _(MutableMapping):

    def items(self):            # O(n)
        for i in self:
            yield i[0], i[1]
