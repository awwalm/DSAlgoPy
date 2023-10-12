"""Code Fragment 8.28: An EulerTour base class providing a framework
for performing Euler tour traversals of a tree."""

from typing import Union, Any
from Goodrich.Chapter8.tree import Tree
from Goodrich.Chapter8.binary_tree import BinaryTree


class EulerTour:
    """Abstract base class for performing Euler tour of a tree.\n
    ``_hook_previsit`` and ``_hook_postvisit`` may be overridden by subclasses.
    """
    def __init__(self, tree: Union[Tree, BinaryTree]):
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

    def _tour(self, p: Tree.Position, d: int, path: list) -> Union[None, Any]:
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
        pass                                            # Can be overridden

    def _hook_postvisit(self, p: Tree.Position, d: int, path: list, results: list):
        pass                                            # Can be overridden


# Code Fragment 8.29: A subclass of EulerTour that produces an indented preorder list of a tree’s elements.
class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p: Tree.Position, d: int, path: list):
        print(2*d*" " + str(p.element()))
    def _hook_postvisit(self, p: Tree.Position, d: int, path: list, results: list):
        label = ".".join(str(j+1) for j in path)        # Labels are one-indexed
        print(2*d*" " + label, p.element())


# Code Fragment 8.31: A subclass of EulerTour that prints a parenthetic string representation of a tree.
class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p: Tree.Position, d: int, path: list):
        if path and path[-1] > 0:                       # p follows a sibling
            print(", ", end="")                         # So preface with comma
        print(p.element(), end="")                      # Then print element
        if not self.tree().is_leaf(p):                  # If p has children
            print(" (", end="")                         # Print opening parenthesis
    def _hook_postvisit(self, p: Tree.Position, d: int, path: list, results: list):
        if not self.tree().is_leaf(p):                  # If p has children
            print(")", end="")                          # Print closing parenthesis


# Code Fragment 8.32: A subclass of EulerTour that computes disk space for a tree.
class DiskSpaceTour(EulerTour):
    def _hook_postvisit(self, p: Tree.Position, d: int, path: list, results: list):
        # We simply add space associated with p to that of its subtrees
        return p.element().space() + sum(results)


# Code Fragment 8.33: A BinaryEulerTour base class providing a specialized tour for binary trees.
# The original EulerTour base class was given in Code Fragment 8.28.
class BinaryEulerTour(EulerTour):
    """Abstract base class for performing Euler tour of a binary tree.

    This version includes an additional _hook_visit that is called after the tour
    of the left subtree (if any), yet before the tour of the right subtree (if any).

    NOTE: Right child is always assigned index 1 in path, even if no left sibling.
    """
    def _tour(self, p: Tree.Position, d: int, path: list):
        results = [None, None]                          # Will update with results of recursions
        self._hook_previsit(p, d, path)                 # "Pre visit" for p
        if self._tree.left(p) is not None:              # Consider left child
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p, d, path)                  # "In visit" for p
        if self._tree.right(p) is not None:             # Consider right child
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(                  # "Post visit" p
            p, d, path, results)
        return answer

    # @TODO: Goodrich and co. provided a awfully weak explanation of the purpose of the invisit.
    # @TODO (contd.) Thus, the assumption is it simply carries the logic for a node without siblings.
    def _hook_invisit(self, p, d, path): pass           # Can be overridden

