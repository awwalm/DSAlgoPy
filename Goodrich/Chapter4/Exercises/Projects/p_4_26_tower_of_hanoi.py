"""This version of the Tower of Hanoi solution uses ``Stacks`` to print all disks for every move made.

In the Towers of Hanoi puzzle, we are given a platform with three pegs, a, b, and c.
On peg a is a stack of n disks, each larger than the next, so that the smallest is on the top
and the largest is on the bottom. The puzzle is to move all the disks from peg a to peg c,
moving one disk at a time, so that we never place a larger disk on top of a smaller one.
"""


class TowerStack:
    """A ``Stack``-based structure for processing disk removal (``pop``) and insertion (``push``)."""
    def __init__(self, size: int, tower: str):
        self.tower = tower
        if size < 1:
            self.items = []
        else:
            self.items = [i for i in range(size, 0, -1)]

    def pop(self):
        popped = self.items[-1]
        self.items = self.items[:-1]
        return popped

    def push(self, item):
        self.items.append(item)


class HanoiTowers:
    def __init__(self, disk: int, source: str, intermediate: str, destination: str):
        assert disk <= 64, "We stick to the 64-disk limit originally invented for the game"
        self.disk = disk
        self.source = TowerStack(disk, source)
        self.intermediate = TowerStack(0, intermediate)
        self.destination = TowerStack(0, destination)
        self._hanoi(self.disk, self.source, self.intermediate, self.destination)

    # noinspection PyMethodMayBeStatic
    def _display_towers(self, a: TowerStack, b: TowerStack, c: TowerStack):
        """Helper method for printing the contents (disks) on all towers (stacks), side by side.
        It uses **Breadth-First (or row-order) Traversal** across all three stacks with respect due
        to the longest stack. This implies disks from stacks smaller than the biggest stack
        are padded with empty strings across the iteration or traversal when the index is illegal.
        """
        disks = [len(a.items), len(b.items), len(c.items)]
        towers = [a, b, c]
        for i in towers:
            if i.tower == "A":
                a = i
            elif i.tower == "B":
                b = i
            elif i.tower == "C":
                c = i

        for i in range(max(disks)-1, -1, -1):
            x = "" if i > len(a.items)-1 else a.items[i]
            y = "" if i > len(b.items)-1 else b.items[i]
            z = "" if i > len(c.items)-1 else c.items[i]
            print("\t%+6s %+6s %+6s" % (x, y, z))

        base = "-" * 24
        tower_names = "\t%+6s %+6s %+6s" % ("A", "B", "C")
        print(f"\t{base}\n{tower_names}\n")

    def _hanoi(self, disk: int, source: TowerStack, intermediate: TowerStack, destination: TowerStack):
        """Prints the move of each disk across the towers recursively.\n
        :param disk:            The initial disks on the contemporary source tower.
        :param source:          The contemporary source tower a disk move starts from.
        :param intermediate:    A varying provisional storage tower.
        :param destination:     The contemporary destination tower a disk is moved to.
        """
        if disk == 1:
            print(f"Disk {disk} moved from Tower {source.tower} to {destination.tower}.")
            destination.push(source.pop())
            self._display_towers(source, intermediate, destination)
        else:
            self._hanoi(disk=disk - 1, source=source, intermediate=destination, destination=intermediate)
            print(f"Disk {disk} moved from Tower {source.tower} to {destination.tower}.")
            destination.push(source.pop())
            self._display_towers(source, intermediate, destination)
            self._hanoi(disk=disk - 1, source=intermediate, intermediate=source, destination=destination)


# Prints (2^disk)-1 moves, i.e. 15 moves when n=4.
HanoiTowers(disk=2, source="A", intermediate="B", destination="C")
