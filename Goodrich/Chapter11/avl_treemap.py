"""Code Fragment 11.12/13: AVLTreeMap class."""
from Goodrich.Chapter11.treemap import TreeMap


class AVLTreeMap(TreeMap):
    """Sorted map implementation using an AVL tree."""

    # Nested _Node class ----------------------------------------------------------------
    class _Node(TreeMap._Node):
        """Node class for AVL maintains height value for balancing."""
        __slots__ = "_height"                           # Additional data member to store height

        def __init__(self, element, parent=None, left=None, right=None):
            super(AVLTreeMap._Node, self).__init__(element, parent, left, right)
            self._height = 0                            # Will be recomputed during balancing

        @property
        def node_height(self):
            return self._height

        @node_height.setter
        def node_height(self, value):
            self._height = value

        def left_height(self):
            return self._left.node_height if self._left is not None else 0

        def right_height(self):
            return self._right.node_height if self._right is not None else 0

    # Positional-based utility methods ---------------------------------------------------
    # noinspection PyMethodMayBeStatic
    def _recompute_height(self, p):
        p.node.node_height = 1 + max(p.node.left_height(), p.node.right_height())

    # noinspection PyMethodMayBeStatic
    def _isbalanced(self, p):
        return abs(p.node.left_height() - p.node.right_height()) <= 1

    def _tall_child(self, p, favorleft = False):
        if p.node.left_height() + (1 if favorleft else 0) > p.node.right_height():
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        # If child is on left, favor left grandchild; else favor right grandchild
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        while p is not None:
            old_height = p.node.node_height                 # Trivially 0 if new node
            if not self._isbalanced(p):                     # Imbalance detected!
                # Perform trinode restructuring, setting p to resulting root,
                # and recompute new local heights after restructuring
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)                       # Adjust for recent changes
            if p.node.node_height == old_height:            # Has height changed
                p = None                                    # No further changes needed
            else:
                p = self.parent(p)                          # Repeat with parent

    # Override balancing hooks ------------------------------------------------------------
    def _rebalance_insert(self, p):
        self._rebalance(p)
