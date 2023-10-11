"""Code Fragment 8.28: An EulerTour base class providing a framework
for performing Euler tour traversals of a tree."""
from Goodrich.Chapter8.tree import Tree


class EulerTour:
    """Abstract base class for performing Euler tour of a tree.\n
    ``_hook_previsit`` and ``_hook_postvisit`` may be overridden by subclasses.
    """
    def __init__(self, tree: Tree):
        """Prepare an Euler tour template for given tree."""
        self._tree = tree

    def tree(self):
        """Return reference to the tree being traversed."""
        return self._tree

    def execute(self):
        """Perform the tour and return any result from post visit of root."""
        if len(self._tree) > 0:
            return self._tour(
                self._tree.root(), 0, [])       # Start the recursion

    def _tour(self, p: Tree.Position, d: int, path: list):
        """Perform tour of subtree rooted at Position p.
        :param p:       Position of current node being visited.
        :param d:       Depth of p in the tree.
        :param path:    List of indices of children on path from root to p.
        """
        self._hook_previsit(p, d, path)                 # "Pre visit" p
        results = []
        path.append(0)                                  # Add new index to end of path before recursion
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))    # Recur on child's subtree
            path[-1] += 1                               # Increment index
        path.pop()                                      # Remove extraneous index from end of path
        answer = self._hook_postvisit(
            p, d, path, results)                        # "Post visit" p
        return answer

    def _hook_previsit(self, p: Tree.Position, d: int, path: list):
        # Can be overridden
        pass

    def _hook_postvisit(self, p: Tree.Position, d: int, path: list, results: list):
        # Can be overridden
        pass
