from __future__ import annotations

class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    # Nested _Item class ------------------------------------------------------------------
    class _Item:
        """Lightweight composite to store prority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other: PriorityQueueBase._Item):
            return self._key < other._key           # Compare items based on their keys

        @property
        def key(self):
            return self._key

        @property
        def value(self):
            return self._value

    # Concrete method(s) ------------------------------------------------------------------
    # noinspection PyTypeChecker
    def is_empty(self):                             # Concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self) == 0
