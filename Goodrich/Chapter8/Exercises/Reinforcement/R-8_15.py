"""R-8.15: The LinkedBinaryTree class provides only nonpublic versions of the update methods
 discussed on page 319. Implement a simple subclass named MutableLinkedBinaryTree that provides
  public wrapper functions for each of the inherited nonpublic update methods."""
from Goodrich.Chapter8.linked_binary_tree import LinkedBinaryTree


class MutableLinkedBinaryTree(LinkedBinaryTree):
    """Provides public wrapper functions for each of the inherited nonpublic update methods."""

    def add_root(self, e):
        return self._add_root(e)

    def add_left(self, p, e):
        return self._add_left(p, e)

    def add_right(self, p, e):
        return self._add_right(p, e)

    def replace(self, p, e):
        return self._replace(p, e)

    def delete(self, p):
        return self._delete(p)

    def attach(self, p, T1, T2):
        return self.attach(p, T1, T2)
