"""An implementation of a DynamicArray class, using a raw array from the ctypes module as storage.
"""
import ctypes


# noinspection PyMethodMayBeStatic
class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Creates an empty array."""
        self._n = 0                                             # Count actual elements.
        self._capacity = 1                                      # Default array capacity.
        self._A = self._make_array(self._capacity)              # Low-level array.

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index ``k``.\n
        :raises IndexError: when ``k`` is not in range.
        """
        if not 0 <= k < self._n:
            raise IndexError("Invalid index")
        return self._A[k]                                       # Retrieve from array.

    # @FIXME: Fix docstring for linking class methods
    def append(self, obj):
        """Add object to end of the array\n.
        :py:func: see also - `~dynamic_array.DynamicArray._make_array`
        """
        if self._n == self._capacity:                           # If not enough room.
            self._resize(2 * self._capacity)                    # Double capacity.
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity ``c``."""
        B = self._make_array(c)                                 # New (bigger) array.
        for k in range(self._n):                                # For each existing value...
            B[k] = self._A[k]
        self._A = B                                             # Use the bigger array.
        self._capacity = c

    def _make_array(self, c):
        """Return new array with capacity ``c``."""
        return (c * ctypes.py_object)()
