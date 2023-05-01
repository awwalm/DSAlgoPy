"""In the Towers ofHanoi puzzle, we are given a platform with three pegs, a, b,and c.
On peg a is a stack of n disks, each larger than the next, so that the smallest is on the top
and the largest is on the bottom. The puzzle is to move all the disks from peg a to peg c, moving one disk at a time,
so that we never place a larger disk on top of a smaller one. See Figure 4.15 for an example of the case n = 4.
Describe a recursive algorithm for solving the Towers of Hanoi puzzle for arbitrary n.
(Hint: Consider first the subproblem of moving all but the nth disk from peg a to another peg
using the third as temporary storage.)
"""


def hanoi(disk: int, source: str, intermediate: str, destination: str):
    """Prints the move of each disk across the towers recursively.\n
    :param disk:            The initial disks on the contemporary source tower.
    :param source:          The contemporary source tower a disk move starts from.
    :param intermediate:    A varying provisional storage tower.
    :param destination:     The contemporary destination tower a disk is moved to.
    """
    if disk == 1:
        print(f"Disk {disk} moved from Tower {source} to {destination}.")
    else:
        hanoi(disk=disk - 1, source=source, intermediate=destination, destination=intermediate)
        print(f"Disk {disk} moved from Tower {source} to {destination}.")
        hanoi(disk=disk - 1, source=intermediate, intermediate=source, destination=destination)
