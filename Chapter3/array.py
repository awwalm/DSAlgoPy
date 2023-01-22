"""Implementation of the ``MultiArray`` ADT using a 1-D array."""
from Chapter2.array import Array


class MultiArray:
    """Creates a multi-dimensional array."""

    def __init__(self, *dimensions):
        assert len(dimensions) > 1, "The array must have 2 or more dimensions."
        # The variable argument tuple contains the dim sizes.
        self._dims = dimensions
        # Compute the total number of elements in the array.
        size = 1
        for d in dimensions:
            assert d > 0, "Dimensions must be > 0."
            size *= d
        # Create the 1-D array to store the elements.
        self._elements = Array(size)
        # Create a 1-D array to store the equation factors.
        self._factors = Array(len(dimensions))
        self._computeFactors()

    def numDims(self):
        """Returns the number of dimensions in the array."""
        return len(self._dims)

    def length(self, dim):
        """Returns the length of the given dimension."""
        assert 1 <= dim < len(self._dims), "Dimension component out of range."
        return self._dims[dim - 1]

    def clear(self, value):
        """Clears the array by setting all elements to the given value."""
        self._elements.clear(value)

    def __getitem__(self, ndxTuple):
        """Returns the contents of element (i_1, i_2, ..., i_n)."""
        assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts."
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range."
        return self._elements[index]

    def __setitem__(self, ndxTuple, value):
        """Sets the contents of element (i_1, i_2, ..., i_n)."""
        assert len(ndxTuple) == self.numDims(), "Invalid # array subscripts."
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range."
        self._elements[index] = value

    def _computeIndex(self, idx):
        """
        Computes the 1-D array offset for element  (i_1, i_2, ... i_n)
        using the equation i_1 * f_1 + i_2 * f_2 + ... + i_n * f_n.
        """
        offset = 0
        for j in range(len(idx)):
            # Make sure the index components are within the legal range.
            if idx[j] < 0 | idx[j] >= self._dims[j]:
                return None
            else:  # sum the product of i_j * f_j.
                offset += idx[j] * self._factors[j]
        return offset

    def _computeFactors(self):
        """Computes the factor values used in the index equation."""
        ...
