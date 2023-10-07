"""Code Fragment 8.1/8.2: A portion of our Tree abstract base class."""
from typing import Union, Iterable
from Goodrich.Chapter7.linked_queue import LinkedQueue


class Tree:
    """Abstract base class represeting a tree structure."""

    # Nested Position methods ------------------------------------------------------------------
    class Position:
        """An abstraction represening the location of a single element."""
        def element(self):
            """Return the element stored at this ``Position``."""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """Return ``True`` if other ``Position`` represents the same location."""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            """Return ``True`` if other does not represent the same location."""
            return not (self == other)                                      # Opposite of __eq__

    # Abstract methods that concrete subclass must support -------------------------------------
    def root(self) -> Union[Position, None]:
        """Return ``Position`` representing the tree's root (or None if empty)."""
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p: Position) -> Union[Position, None]:
        """Return ``Position`` representing p's parent (or None if p is root)."""
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p: Position) -> int:
        """Return the number of children that ``Position`` p has."""
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p: Position) -> Iterable[Position]:
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError("must be implemented by subclass")

    # Concrete methods implemented in this class -----------------------------------------------
    def is_root(self, p: Position):
        """Return ``True`` if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p: Position):
        """Return ``True`` if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return ``True`` if the tree is empty."""
        return len(self) == 0

    def depth(self, p: Position):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        """Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p: Position):  # Time is linear (or in size) of subtree
        """Return the height of the subtree rooted a Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.\n
        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p)  # Start _height2 recursion

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):       # Start recursion
                yield p

    def _subtree_preorder(self, p: Position):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p                                                 # Visit p before its subtrees
        for c in self.children(p):                              # For each child c
            for other in self._subtree_preorder(c):             # Do preorder of c's subtree
                yield other                                     # Yielding each to our caller

    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.preorder()                                  # Return entire preorder iteration

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):      # Start recursion
                yield p

    def _subtree_postorder(self, p: Position):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):                              # For each child c
            for other in self._subtree_postorder(c):            # Do postorder of c's subtree
                yield other                                     # Yielding each to our caller
        yield p                                                 # Visit p after its subtrees

    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p: Tree.Position = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)
