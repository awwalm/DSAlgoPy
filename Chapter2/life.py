"""Implements the ``LifeGrid`` ADT for use with the game of Life."""

from array import Array2D


class LifeGrid:
    """Defines constants to represent the cell states."""

    def __init__(self, numRows, numCols):
        self._numRows = numRows
        self._numCols = numCols
        # Allocate the 2-D array for the grid.
        self._grid = Array2D(numRows, numCols)
        # Clear the grid and set all cells to dead.
        self.configure(list())

    def numRows(self):
        """Returns the number of rows in the grid."""
        return self._grid.numRows()

    def numCols(self):
        """Returns the number of columns in the grid."""
        return self._grid.numCols()

    def configure(self, coordList):
        """Configures the grid to contain the given live cells."""

        # Clear the game grid.
        for i in range(self._numRows):
            for j in range(self._numCols):
                self.clearCell(i, j)

        # Set the indicated cells to be alive.
        for coord in coordList:
            self.setCell(coord[0], coord[1])

    def isLiveCell(self, row, col):
        """Does the indicated cell contain a live organism?"""
        return self._grid[row, col] == GameGrid.LIVE_CELL

    def clearCell(self, row, col):
        """Clears the indicated cell by setting it to dead."""
        self._grid[row, col] = GameGrid.DEAD_CELL

    def setCell(self, row, col):
        """Sets the indicated cell to be alive."""
        self._grid[row, col] = GameGrid.LIVE_CELL

    def numLiveNeighbors(self, row, col):
        """Returns the number of live neighbor for the given cell."""
        ...


class GameGrid:
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self):
        pass
