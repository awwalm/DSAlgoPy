"""Code Fragment 11.14: A complete implementation of the SplayTreeMap class."""
from Goodrich.Chapter11.treemap import TreeMap


class SplayTreeMap(TreeMap):
    """Sorted map implementation using a splay tree."""
    # Splay operation ----------------------------------------------------------------
    def _splay(self, p: TreeMap.Position):
        while p != self.root():
            parent = self.parent(p)
            grand = self.parent(parent)
            if grand is None:
                # Zig case
                self._rotate(p)
            elif (parent == self.left(grand)) == (p == self.left(parent)):
                # Zig-zag case
                self._rotate(parent)                    # Move PARENT up
                self._rotate(p)                         # Then move p up
            else:
                # Zig-zag case
                self._rotate(p)                         # Move p up
                self._rotate(p)                         # Move p up again

    # Override balancing hooks --------------------------------------------------------
    def _rebalance_insert(self, p: TreeMap.Position):
        self._splay(p)

    def _rebalance_delete(self, p: TreeMap.Position):
        if p is not None:
            self._splay(p)

    def _rebalance_access(self, p: TreeMap.Position):
        self._splay(p)
