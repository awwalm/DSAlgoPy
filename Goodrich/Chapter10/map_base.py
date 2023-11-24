"""Code Fragment 10.2: Extending the MutableMapping abstract base class to provide
a nonpublic Item class for use in our various map implementations."""
from __future__ import annotations
from collections.abc import MutableMapping


# noinspection PyAbstractClass
class MapBase(MutableMapping):
    """Abstract base class that includes a non-public ``_Item`` class."""
    # Nested _Item class ----------------------------------------------------------------
    class _Item:
        """Lightweight composite to store key-value pairs as map items."""
        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other: MapBase._Item):
            return self._key == other._key          # Compare items based on their keys

        def __ne__(self, other: MapBase._Item):
            return not (self == other)              # Opposite of __eq__

        def __lt__(self, other: MapBase._Item):
            return self._key < other._key           # Compare items based on their keys

        @property
        def key(self):
            return self._key

        @property
        def value(self):
            return self._value
