"""Code Fragment 11.15/17: Beginning of the RedBlackTreeMap class."""
from __future__ import annotations
from Goodrich.Chapter11.treemap import TreeMap


# noinspection PyMethodMayBeStatic
class RedBlackTreeMap(TreeMap):
    """Sorted map implementation using a red-black tree."""

    # Nested _Node subclass -----------------------------------------------------------------
    class _Node(TreeMap._Node):
        """Node class for red-black tree maintains bit that denotes color."""
        __slots__ = "_red"                              # Add additional information to the Node class

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._red = True                            # New node red by default

        @property
        def red(self):
            return self._red

    # Positional-based utilities -----------------------------------------------------------
    # We consider a nonexistent child to be trivially black.
    def _set_red(self, p: RedBlackTreeMap.Position): p.node._red = True
    def _set_black(self, p: RedBlackTreeMap.Position): p.node._red = False
    def _set_color(self, p: RedBlackTreeMap.Position, make_red): p.node._red = make_red
    def _is_red(self, p: RedBlackTreeMap.Position): return p is not None and p.node.red
    def _is_red_leaf(self, p: RedBlackTreeMap.Position): return self._is_red(p) and self.is_leaf(p)

    def _get_red_child(self, p: RedBlackTreeMap.Position):
        """Return a red child of p (or None if no such child)."""
        for child in (self.left(p), self.right(p)):
            if self._is_red(child):
                return child
        return None

    # Support for insertions ---------------------------------------------------------------
    def _rebalance_insert(self, p: RedBlackTreeMap.Position):
        self._resolve_red(p)                            # New node is always red

    def _resolve_red(self, p: RedBlackTreeMap.Position):
        if self.is_root(p):
            self._set_black(p)                          # Make root black
        else:
            parent = self.parent(p)
            if self._is_red(parent):                    # Double red problem
                uncle = self.sibling(parent)
                if not self._is_red(uncle):             # Case 1: Mis-shapen 4-node
                    middle = self._restructure(p)       # Do trinode restructuring
                    self._set_black(middle)             # And then fix colors
                    self._set_red(self.left(middle))
                    self._set_red(self.right(middle))
                else:
                    grand = self.parent(parent)         # Case 2: Overfull 5-node
                    self._set_red(grand)
                    self._set_black(self.left(grand))   # Grandparent becomes red
                    self._set_black(self.right(grand))  # Its children become black
                    self._resolve_red(grand)            # Recur at red grandparent

    # Support for deletions ---------------------------------------------------------------
    def _rebalance_delete(self, p: RedBlackTreeMap.Position):
        if len(self) == 1:
            self._set_black(self.root())                # Special case: ensure that root is black
        elif p is not None:
            n = self.num_children(p)
            if n == 1:                                  # Deficit exists unless child is a red leaf
                c = next(self.children(p))
                if not self._is_red_leaf(c):
                    self._fix_deficit(p, c)
            elif n == 2:                                # Removed black node with red child
                if self._is_red_leaf(self.left(p)):
                    self._set_black(self.left(p))
                else:
                    self._set_black(self.right(p))

    def _fix_deficit(self, z, y):
        """Resolve black deficit at z, where y is the root of z's heavier subtree."""
        if not self._is_red(y):                         # y is black; will apply Case 1 or 2
            x = self._get_red_child(y)
            if x is not None:   # Case 1: y is black and has red child x; do "transfer"
                old_color = self._is_red(z)
                middle = self._restructure(x)
                self._set_color(middle, old_color)
                self._set_black(self.left(middle))
                self._set_black(self.right(middle))
            else:               # Case 2: y is black, but no red children; recolor as "fusion"
                self._set_red(y)
                if self._is_red(z):
                    self._set_black(z)                  # This resolves the problem
                elif not self.is_root(z):
                    self._fix_deficit(
                        self.parent(z), self.sibling(z))    # Recur upward
        else:   # Case 3: y is red; rotate misaligned 3-node and repeat
            self._rotate(y)
            self._set_black(y)
            self._set_red(z)
            if z == self.right(y):
                self._fix_deficit(z, self.left(z))
            else:
                self._fix_deficit(z, self.right(z))
