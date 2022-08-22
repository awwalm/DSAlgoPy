from array import Array2D


class Matrix:
    """Implementation of the Matrix ADT using a 2-D array."""

    def __init__(self, numRows, numCols):
        """Creates a matrix of size numRows x numCols initialized to 0."""
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)

    def numRows(self):
        """Returns the number of rows in the matrix."""
        return self._theGrid.numRows()

    def numCols(self):
        """Returns the number of columns in the matrix."""
        return self._theGrid.numCols()

    def __getitem__(self, ndxTuple):
        """Returns the value of element (i, j): x[i, j]."""
        return self._theGrid[ndxTuple[0], ndxTuple[1]]

    def __setitem__(self, ndxTuple, scalar):
        """Sets the value of element (i, j) to the value s: x[i, j] = s."""
        self._theGrid[ndxTuple[0], ndxTuple[1]] = scalar

    def scaleBy(self, scalar):
        """Scales the matrix by the given scalar."""
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] *= scalar

    def transpose(self):
        """Creates and returns a new matrix that is the transpose of this matrix."""
        ...

    def __add__(self, rhsMatrix):
        """Creates and returns a new Matrix that results from matrix addition."""
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols() == self.numCols(), \
            "Matrix sizes not compatible for the add operation."
        # Create the new matrix.
        newMatrix = Matrix(self.numRows(), self.numCols())
        # Add the corresponding elements in the two matrices.
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c] + rhsMatrix[r, c]
        return newMatrix

    def __sub__(self, rhsMatrix):
        """Creares and returns a new Matrix that results from matrix subtraction."""
        ...

    def __mul__(self, rhsMatrix):
        """Creates and returns a new matrix resultng from matrix multiplication."""
        ...
