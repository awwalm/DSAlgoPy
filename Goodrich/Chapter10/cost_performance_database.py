"""Code Fragment 10.11:
An implementation of a class maintaining a set of maxima cost-performance pairs using a sorted map."""
from Goodrich.Chapter10.sorted_table_map import SortedTableMap


class CostPerformanceDatabase:
    """Maintain a database of maximal (cost,performance) pairs."""

    def __init__(self):
        """Create an empty database."""
        self._M = SortedTableMap()                       # Or a more efficient sorted map

    def best(self, c):
        """Return (cost,performance) pair with the largest cost not exceeding c.\n
        :return: None - if there is no such pair.
        """
        return self._M.find_le(c)                       # RANKING CRITERIA IS THE INDEX OF c

    def add(self, c, p):
        """Add new entry with cost c and performance p."""
        # Determine if (c,p) is dominated by an existing pair.
        other = self._M.find_le(c)                      # Other is at least as cheap as c

        # Check if prive (value returned by existing key as good as c) is as good as new price to be added.
        if other is not None and other[1] >= p:         # If its performance is as good,
            return                                      # (c,p) is dominated, so ignore
        self._M[c] = p                                  # Else, add (c,p) to database

        # And now, remove any pairs that are dominated by (c,p). @FIXME : why!!??
        other = self._M.find_gt(c)                      # Other more expensive than c
        while other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_gt(c)
