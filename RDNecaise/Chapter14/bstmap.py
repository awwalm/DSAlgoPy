from RDNecaise.Chapter2.array import Array
from RDNecaise.Chapter7.lliststack import Stack


class BSTMap:
    """Creates an empty map instance."""
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        """Returns the number of entries in the map."""
        return self._size

    def __iter__(self):
        """Returns an iterator for traversing the keys in the map."""
        return _BSTMapIterator(self._root)

    def __contains__(self, key):
        """Determines if the map contains the given key."""
        return self._bstSearch(self._root, key) is not None

    def valueOf(self, key):
        """Returns the value associated with the key."""
        node = self._bstSearch(self._root, key)
        assert node is not None, f"Invalid map key: {key}"
        return node.value

    def _bstSearch(self, subtree, target):
        """Helper method that recursively searches the tree for a target key."""
        if subtree is None:                         # Base case
            return None
        elif target < subtree.key:                  # Target is left of the subtree root
            return self._bstSearch(subtree.left, target)
        elif target > subtree.key:                  # Target is right of the subtree root
            return self._bstSearch(subtree.right, target)
        else:                                       # Base case
            return subtree

    def _bstMinimum(self, subtree):
        """Helper method for finding the node containing the minimum key."""
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bstMinimum(subtree.left)

    def _bstMaximum(self, subtree):
        """Symmetric reflection of ``_bstMinimum()``."""
        if subtree is None:
            return None
        elif subtree.right is None:
            return subtree
        else:
            return self._bstMaximum(subtree)

    def add(self, key, value):
        """Adds a new entry to the map or replaces the values of an existing key."""
        node = self._bstSearch(self._root, key)     # Find the node containing the key, if it exists
        if node is not None:                        # If the key is already in the tree, update its value
            node.value = value
            return False
        else:                                       # Otherwise, add a new entry
            self._root = self._bstInsert(self._root, key, value)
            self._size += 1
            return True

    def _bstInsert(self, subtree, key, value):
        """Helper method that inserts a new item, recursively."""
        if subtree is None:
            subtree = _BSTMapNode(key, value)
        elif key < subtree.key:
            subtree.left = self._bstInsert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bstInsert(subtree.right, key, value)
        return subtree

    def remove(self, key):
        """Removes the map entry associated with the given key."""
        assert key in self, "Invalid map key"
        self._root = self._bstRemove(self._root, key)
        self._size -= 1

    def _bstRemove(self, subtree, target):
        """Helper method that removes an existing item recursively.

        This method works by returning a modified version of the current
        subtree that does not contain the indicated key.
        It uses a *self-correcting* mechanism to crawl and process each node.

        - Precondition: key is in the subtree.
        - Returns: A _BSTNode, or None if this is a leaf that is being removed.
        - See Also: https://w3.cs.jmu.edu/spragunr/CS240_F12/lectures/maps/bst_map.py
        """
        if subtree is None:
            return subtree
        elif target < subtree.key:
            subtree.left = self._bstRemove(subtree.left, target)
            return subtree
        elif target > subtree.key:
            subtree.right = self._bstRemove(subtree.right, target)
            return subtree
        else:                                                       # Found node containing target key
            if subtree.left is None and subtree.right is None:      # Key is in a leaf node
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:                        # Key has only a left child
                    return subtree.left
                else:                                               # Key has only a right child
                    return subtree.right
            else:                                                   # Key has two children
                successor = self._bstMinimum(subtree.right)
                subtree.key = successor.key
                subtree.value = successor.value
                # Now that there are two copies, delete the extra copy (assign to none or unlink)
                subtree.right = self._bstRemove(subtree.right, successor.key)
                return subtree


class _BSTMapNode:
    """Storage class for the binary search tree nodes of the map."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class _BSTMapIterator:
    """An iterator for the binary search tree using a Stack ADT."""

    def __init__(self, root):
        """Create a stack for use in traversing the tree."""
        self._theStack = Stack()
        self._traverseToMinNode(root)

    def __iter__(self):
        return self

    def __next__(self):
        if self._theStack.isEmpty():
            raise StopIteration
        else:
            node = self._theStack.pop()
            key = node.key
            if node.right is not None:
                self._traverseToMinNode(node.right)
    def _traverseToMinNode(self, subtree):
        if subtree is not None:
            self._theStack.push(subtree)
            self._traverseToMinNode(subtree.left)


class _BSTMapArrayIterator:
    """An iterator for the binary search tree using an array."""

    def __init__(self, root, size):
        """Creates the array and fills it with the keys."""
        self._theKeys = Array(size)
        self._curItem = 0                       # Keep track of the next location in array
        self._bstTraversal(root)
        self._curItem = 0                       # Reset the current item index

    def __iter__(self):
        return self

    def __next__(self):
        """Returns the next key from the array of keys."""
        if self._curItem < len(self._theKeys):
            key = self._theKeys[self._curItem]
            self._curItem += 1
            return key
        else:
            raise StopIteration

    def _bstTraversal(self, subtree):
        """Performs an inorder traversal used to build the array of keys."""
        if subtree is not None:
            self._bstTraversal(subtree.left)
            self._theKeys[self._curItem] = subtree.key
            self._curItem += 1
            self._bstTraversal(subtree.right)
