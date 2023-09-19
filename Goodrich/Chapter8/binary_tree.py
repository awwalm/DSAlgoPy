"""Code Fragment 8.7: A Binary Tree abstract base class that extends the existing ``Tree``
abstract base class from Code Fragments 8.1 and 8.2."""
from Goodrich.Chapter8.tree import Tree


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # Additional abstract methods --------------------------------------------------------
    def left(self, p: Tree.Position):
        """Return a ``Position`` representing p's left child.
        Return ``None`` if p does not have a left child.
        """
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p: Tree.Position):
        """Return a ``Position`` representing p's right child.
        Return ``None`` if p does not have a right child.
        """
        raise NotImplementedError("must be implemented by subclass")

    # Concrete methods implemented in this class ------------------------------------------
    def sibling(self, p: Tree.Position):
        """Return a ``Position`` representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:                          # p must be the root
            return None                             # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)           # possibly None
            else:
                return self.left(parent)            # possibly None

    def children(self, p: Tree.Position):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
