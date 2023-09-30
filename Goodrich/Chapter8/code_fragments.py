"""Code Fragments for Chapter 8 (⚠ DO NOT EXECUTE DIRECTLY)"""

# Code Fragment 8.3: Method depth of the Tree class.
def depth(self, p):             # Works, but O(n^2) worst-case
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
def _height2(self, p):          # Time is linear (or in size) of subtree
    """Return the height of the subtree rooted a Position p."""
    if self.is_leaf(p):
        return 0
    else:
        return 1 + max(self.height2(c) for c in self.children(p))

# Code Fragment 8.6: Public method Tree.height that computes the height of the entire tree
# by default, or a subtree rooted at a given position, if specified.
def height(self, p=None):
    """Return the height of the subtree rooted at Position p.\n
    If p is None, return the height of the entire tree.
    """
    if p is None:
        p = self.root()
    return self._height2(p)     # Start _height2 recursion

# Code Fragment 8.16: Iterting all elements of a Tree instance, based upon an iteration
# of the positions of the tree. This code should be included in the body of the Tree class.
def __iter__(self):
    """Generate an iteration of the tree's elements."""
    for p in self.positions():
        yield p.element()

