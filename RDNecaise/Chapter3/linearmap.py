"""Implementation of ``Map`` ADT using a single list."""


class Map:
    """Creates an empty map instance."""
    def __init__(self):
        self._entryList = list()

    def __len__(self):
        """Returns the number of entries in the map."""
        return len(self._entryList)

    def __contains__(self, key):
        """Determines if the map contains the given key."""
        ndx = self._findPosition(key)
        return ndx is not None

    def add(self, key, value):
        """
        Adds a new entry to the map if the key does exist. Otherwise, the
        new value replaces the current value associated with the key.
        """
        ndx = self._findPosition(key)
        if ndx is not None:  # if the key was found
            self._entryList[ndx].value = value
            return False
        else:   # otherwise add a new entry
            entry = _MapEntry(key, value)
            self._entryList.append(entry)
            return True

    def valueOf(self, key):
        """Returns the value associated with the key."""
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key."
        return self._entryList[ndx].value

    def remove(self, key):
        """Removes the entry associated with the key."""
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key."
        self._entryList.pop(ndx)

    def __iter__(self):
        """Returns an iterator for traversing the keys in the map."""
        return _MapIterator(self._entryList)

    def __getitem__(self, item):
        """Support for the syntax map[key]."""
        return self.valueOf(item)

    def _findPosition(self, key):
        """
        Helper method used to find the index position of a category.
        If the key is not found, ``None`` is returned.
        """
        # Iterate through each entry in the list.
        for i in range(len(self)):
            # Is the key stored in the ith entry?
            if self._entryList[i].key == key:
                return i
        # When not found, return ``None``.
        return None


class _MapIterator:
    def __init__(self, _map):
        self._mapRef = _map
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._mapRef):
            item = self._mapRef[self._curNdx]
            self._curNdx += 1
            return item
        else:
            raise StopIteration


class _MapEntry:
    """Storage class for holding the key/value pairs."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
