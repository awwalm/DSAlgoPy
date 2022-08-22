import ctypes


class Array2D:
    """
    Implements the ``Array2D`` ADT using `array of arrays` approach.
    Creates a 2-D array of size numRows x numCols.
    """

    def __init__(self, numRows, numCols):
        """Create the 1-D array to store an array reference for each row."""
        self._theRows = Array(numRows)

        # Create the 1-D arrays for each row of the 2-D array.
        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    def numRows(self):
        """Returns the number of rows in the 2-D array."""
        return len(self._theRows)

    def numCols(self):
        """Returns the number of columns in the 2-D array."""
        return len(self._theRows[0])

    def clear(self, value):
        """Clears the array by setting every element to the given value."""
        for row in range(self.numRows()):
            row.clear(value)

    def __getitem__(self, ndxTuple):
        """Gets the contents of the element at position [i, j]."""
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert 0 <= row < self.numRows() and 0 <= col < self.numCols(), "Array subscript out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]

    def __setitem__(self, ndxTuple, value):
        """Sets the contents of the element at position [i, j] to value."""
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert 0 <= row < self.numRows() and 0 <= col < self.numCols(), "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value


class Array:
    """
    Implements the ``Array`` ADT using array capabilities of the ``ctypes`` module.
    Creates an array with size elements.
    """

    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size

        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()

        # Initialize each element.
        self.clear(None)

    def __len__(self):
        """Returns the size of the array."""
        return self._size

    def __getitem__(self, index):
        """Gets the contents of the index element."""
        assert 0 <= index < len(self), "Array subscript out of range."
        return self._elements[index]

    def __setitem__(self, index, value):
        """Puts the value in the array element at index position."""
        assert 0 <= index < len(self), "Array subscript out of range."
        self._elements[index] = value

    def clear(self, value):
        """Clears the array by setting each element to the given value."""
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """Returns the array's iterator for traversing the elements."""
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    """An iterator for the Array ADT."""

    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration
