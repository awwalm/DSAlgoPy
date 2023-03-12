"""Demonstration of abstract classes via template method pattern."""

from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    """Our own version of ``collections.Sequence`` abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence."""

    def __contains__(self, val):
        """Return ``True`` if val found in the sequence; ``False`` otherwise."""
        for j in range(len(self)):
            if self[j] == val:                       # Found match.
                return True
        return False

    def index(self, val):
        """Return leftmost index at which val is found (or rasie ``ValueError``)."""
        for j in range(len(self)):
            if self[j] == val:                      # Leftmost match.
                return j
        raise ValueError("Value not in sequence")   # Never found a match.

    def count(self, val):
        """Return the number of elements equal to the given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1                              # Found a match.
        return k
