"""Code Fragment 10.17: An implementation of a MultiMap using a dict for storage.
The len method, which returns self. n, is omitted from this listing."""

class MultiMap:
    """A multimap class built upon use of an underlying map for storage."""
    _MapType = dict                             # Map type; can be defined by subclass

    def __init__(self):
        """Create a new empty multimap instance."""
        self._map = self._MapType()             # Create map instance for storage
        self._n = 0

    def __iter__(self):
        """Iterate through all (k,v) pairs in multimap."""
        for k,secondary in self._map.items():
            for v in secondary:
                yield k,v

    def add(self, k, v):
        """Add pair (k,v) to multimap."""
        container = self._map.setdefault(k, []) # Create empty list, if needed
        container.append(v)
        self._n += 1

    def pop(self, k):
        """Remove and return arbitrary (k,v) with key k (or raise KeyError)."""
        secondary = self._map[k]                # May raise KeyError
        v = secondary.pop()
        if len(secondary) == 0:
            del self._map[k]                    # No pairs left
        self._n -= 1
        return k,v

    def find(self, k):
        """Return arbitrary (k,v) pair with given key (or raise KeyError)."""
        secondary = self._map[k]                # May raise KeyError
        return k, secondary[0]

    def find_all(self, k):
        """Generate iteration of all (k,v) pairs with given key."""
        secondary = self._map.get(k, [])        # Empty list, by default
        for v in secondary:
            yield k,v
