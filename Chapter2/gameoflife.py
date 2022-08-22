"""Program for playng the game of Life."""

from life import LifeGrid

# Define the initial configuration of live cells.
INTI_CONFIG = [(1, 1), (1, 2), (2, 2), (3, 2)]

# Set the size of the grid.
GRID_WIDTH, GRID_HEIGHT = 5, 5

# Indicate the number of generations.
NUM_GENS = 8


def main():
    """Construct the game grid and configure it."""
    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INTI_CONFIG)

    # Play the game.
    draw(grid)
    for i in range(NUM_GENS):
        evolve(grid)
        draw(grid)


def evolve(grid):
    """Generates the next generation of organisms."""

    # List for storing the live cells of the next generation.
    liveCells = list()

    # Iterate over the elements of the grid.
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):

            # Determine the number of live neighbors for this cell.
            neighbors = grid.numLiveNeighbors(i, j)

            # Add the (i, j) tuple to liveCells if this cell contains a live organism in the next gen.
            if (neighbors == 2 and grid.isLiveCell(i, j)) or (neighbors == 3):
                liveCells.append((i, j))

    # Reconfigure the grid using the liveCells coord list.
    grid.configure(liveCells)


def draw(grid):
    """Prints a text-based representation of the game grid."""
    ...


# Executes the main function.
main()
