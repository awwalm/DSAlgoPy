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

# Code Fragment 8.23: Efficient recursion for printing indented version of a preorder traversal.
# On a complete tree T, the recursion should be started with form preorder_indent(T, T.root(), 0).
def preorder_indent(T, p, d):
    """Print preorder representation of subtree of T rooted at p at depth d."""
    print(2*d*' ' + str(p.element()))           # Use depth for indentation
    for c in T.children(p):
        preorder_indent(T, c, d+1)              # Child depth is d+1

# Code Fragment 8.24: Efficient recursion for printing an indented and labeled presentation
# of a preorder traversal.
def preorder_label(T, p, d, path):
    """Print labeled representation of subtree of T rooted at p at depth d."""
    label = '.'.join(str(j+1) for j in path)    # Displayed labels are one-indexed
    print(2*d*' ' + label, p.element())
    path.append(0)                              # Path entries are zero-indexed
    for c in T.children(p):
        preorder_label(T, c, d+1, path)         # Child depth is d+1
        path[-1] += 1
    path.pop()

# Code Fragment 8.25: Function that prints prenthetic string representation of a tree.
def parenthesize(T, p):
    """Print parenthesized representation of subtree of T rooted at p."""
    print(p.element(), end='')                  # Use of end avoids trailing newline
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = ' (' if first_time else ', '  # Determine proper separator
            print(sep, end='')
            first_time = False                  # Any future passes will not be the first
            parenthesize(T, c)                  # Recur on child
        print(')', end='')                      # Include closing parenthesis

# Code Fragment 8.26: Recursive computation of disk space for a tree.
# We assume that a space() method of each tree reports the local space used at that position.
def disk_space(T, p):
    """Return total disk space for subtree of T rooted at p."""
    subtotal = p.element().space()              # Space used at position p
    for c in T.children(p):
        subtotal += disk_space(T, c)            # Add child's space to subtotal
    return subtotal

