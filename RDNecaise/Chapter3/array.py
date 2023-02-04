"""Implementation of the ``MultiArray`` ADT using a 1-D array."""
from RDNecaise.Chapter2.array import Array


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

    def factors(self):
        """Returns an array of the computed factors."""
        return self._factors

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
        """
        Computes the factor values used in the index equation.
        Factors are the number of elements to be skipped within the corresponding dimension.
        This should execute prior to calling ``_computeIndex()`` which is called from ``__init__()``.
        This method should populate the factors array with the corresponding factors.

        Recall that given an n-dimensional array:
            * Let F be the collection of Factors and D the collection of numerated Dimensions.
            * f_n = 1, f_n ∈ F
            * F = ∏ d_k ∀ 0<j<n & ∀ d ∈ D
            * ⊨ j+1<=k<= n (i.e the value of k ranges from j+1 to n)
        For example, given a 4-dimensional array:
            * index4(i1, i2, i3, i4) = i1 × (f1 = d2 × d3 × d4) +
                                       i2 × (f2 = d3 × d4) +
                                       i3 × (f3 = d4) +
                                       i4 × (f4 = 1)
        """
        #  -----------------CODE--------------- + --------------------ALGORITHM------------------------
        self._factors[self.numDims()-1] = 1     # As established above, last factor is a constant of 1
        for i in range(self.numDims()-1):       # Initiate index iteration
            temp_dims = self._dims[i+1:]        # Skip the first given dimension
            while len(temp_dims) > 1:           # Make sure we have more than 1 dimension
                temp_dims[0] *= temp_dims[1]    # Multiply by next dimension and store product in [0]
                temp_dims[1] = temp_dims[0]     # Move product from position [0] to [1]
                temp_dims = temp_dims[1:]       # Truncate forwards and repeat until only final product
            self._factors[i] = temp_dims[0]     # Store the current final factor
