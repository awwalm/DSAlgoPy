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

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward.\
        For simplicity, we assume 0 <= k <= n in this version."""
        if self._n == self._capacity:                           # Not enough room.
            self._resize(2 * self._capacity)                    # So double capacity.
        for j in range(self._n, k, -1):                         # Shift rightmost first.
            self._A[j] = self._A[j-1]
        self._A[k] = value                                      # Store newest element.
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of ``value``.\n
        :raises ValueError: if value is not found."""
        for k in range(self._n):
            if self._A[k] == value:                             # Found a match (k; index of value).
                for j in range(k, self._n - 1):                 # Shift others to fill gap.
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None                     # Help garbage collection.
                self._n -= 1                                    # We have one less item.
                return                                          # Exit immediately.
        raise ValueError("Value not found")                     # Only reached if no match.
