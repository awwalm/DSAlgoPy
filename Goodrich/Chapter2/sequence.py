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
            if self[j] == val:
                return True
        return False
