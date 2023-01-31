"""Implements the Bag ADT container using a Python list."""


class Bag:
    def __init__(self):
        """Constructs an empty bag."""
        self._theItems = list()

    def __len__(self):
        """Returns the number of items in the bag."""
        return len(self._theItems)

    def __contains__(self, item):
        """Determines if an item is contained in the bag."""
        return item in self._theItems

    def add(self, item):
        """Adds a new item to the bag."""
        self._theItems.append(item)

    def remove(self, item):
        """Removes and returns an instance of the item from the bag."""
        assert item in self._theItems, "The item must be in the bag."
        ndx = self._theItems.index(item)
        return self._theItems.pop(ndx)

    def __iter__(self):
        """Returns an iterator for traversing the list of items."""
        return _BagIterator(self._theItems)


class _BagIterator:
    """An iterator for the ``Bag`` ADT implemented as a Python list."""
    def __init__(self, theList):
        self._bagItems = theList
        self._curItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration
