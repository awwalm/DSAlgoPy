"""Code Fragments for Chapter 8 (⚠ DO NOT EXECUTE DIRECTLY)"""

# Code Fragment 8.3: Method depth of the Tree class.
def depth(self, p):
    """Return the number of levels separating Position p from the root."""
    if self.is_root(p):
        return 0
    else:
        return 1 + self.depth(self.parent(p))

# Code Fragment 8.4: Method _height1 of the Tree class (calls the depth method).
def _height1(self):
    """Return the height of the tree."""
    return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

# Code Fragment 8.5: Method _height2 for computing the height of a subtree
# rooted at a position p of a Tree.
def _height2(self, p):
    """Return the height of the subtree rooted a Position p."""
    if self.is_leaf(p):
        return 0
    else:
        return 1 + max(self.height2(c) for c in self.children(p))
