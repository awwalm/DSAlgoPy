from typing import Union


# noinspection PyMethodMayBeStatic
class AVLTree:
    """An AVL Tree."""

    # Nonpublic node class -----------------------------------------------------------------
    class _AVLNode:
        __slots__ = "_key", "_value", "_parent", "_left", "_right", "_height"

        def __init__(self, key, value, parent, left=None, right=None, height=0):
            self._key = key
            self._value = value
            self._parent: Union[AVLTree._AVLNode, None] = parent
            self._left: Union[AVLTree._AVLNode, None] = left
            self._right: Union[AVLTree._AVLNode, None] = right
            self._height: int = height

        @property
        def key(self):
            return self._key

        @property
        def value(self):
            return self._value

        @property
        def left(self):
            return self._left

        @property
        def right(self):
            return self._right

        @property
        def parent(self):
            return self._parent

        @property
        def height(self):
            return self._height

        @key.setter
        def key(self, k):
            self._key = k

        @value.setter
        def value(self, v):
            self._value = v

        @left.setter
        def left(self, l):
            self._left = l

        @right.setter
        def right(self, r):
            self._right = r

        @parent.setter
        def parent(self, p):
            self._parent = p

        @height.setter
        def height(self, h):
            self._height = h

    # AVL search tree utilities -----------------------------------------------------------------
    def __init__(self):
        self._root: Union[AVLTree._AVLNode, None] = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, k):
        return True if k == self.search(k, self._root)[0].key else False

    def root(self):
        return self._root

    def is_empty(self):
        return self._size == 0

    def search(self, key, subtree: _AVLNode):
        if key == subtree.key:
            return subtree, True   # Successful search
        elif key < subtree.key:
            if subtree.left is not None:
                return self.search(key, subtree.left)
        else:
            if subtree.right is not None:
                return self.search(key, subtree.right)
        return subtree, False    # Unsuccessful search

    def insert(self, key, value):
        if self.is_empty():
            self._root = self._AVLNode(key, value, None)
            self._size += 1
        else:
            node, found = self.search(key, self._root)
            if found:
                node.value = value
            else:
                if key < node.key:
                    node.left = self._AVLNode(key, value, node)
                else:
                    node.right = self._AVLNode(key, value, node)
                self._size += 1
                self._rebalance(node)

    def _update_height(self, node: _AVLNode):
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _get_height(self, node: _AVLNode):
        return node.height if node else -1

    def _get_balance(self, node: _AVLNode):
        return self._get_height(node.left) - self._get_height(node.right)

    def _rebalance(self, node: _AVLNode):
        while node:
            self._update_height(node)
            if self._get_balance(node) == -2:
                if self._get_balance(node.right) == 1:
                    self._rotate_right(node.right)
                self._rotate_left(node)
            elif self._get_balance(node) == 2:
                if self._get_balance(node.left) == -1:
                    self._rotate_left(node.left)
                self._rotate_right(node)
            node = node.parent

    def delete(self, key):
        self._root = self._delete_recursive(key, self._root)

    def _delete_recursive(self, key, node):
        if node is None:
            return node

        # If the key to be deleted is smaller than the node's key,
        # then it lies in the left subtree.
        if key < node.key:
            node.left = self._delete_recursive(key, node.left)

        # If the key to be deleted is greater than the node's key,
        # then it lies in the right subtree.
        elif key > node.key:
            node.right = self._delete_recursive(key, node.right)

        # If key is the same as node's key, then this is the node to be deleted.
        else:
            # Node with only one child or no child.
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree).
            successor = self._find_min(node.right)

            # Copy the inorder successor's content to this node.
            node.key = successor.key
            node.value = successor.value

            # Delete the inorder successor.
            node.right = self._delete_recursive(successor.key, node.right)

        # Update the height of the current node.
        self._update_height(node)

        # Balance the tree after deletion.
        return self._balance(node)

    def _find_min(self, node: _AVLNode):
        current = node
        while current.left:
            current = current.left
        return current

    def _balance(self, node: _AVLNode):
        # Check balance factor.
        balance = self._get_balance(node)

        # Left heavy subtree
        if balance > 1:
            # Left-right case
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            # Left-left case
            return self._rotate_right(node)

        # Right heavy subtree
        if balance < -1:
            # Right-left case
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            # Right-right case
            return self._rotate_left(node)

        return node

    def _rotate_left(self, node: _AVLNode):
        # Perform left rotation.
        right_child = node.right
        node.right = right_child.left
        if right_child.left:
            right_child.left.parent = node
        right_child.parent = node.parent
        if not node.parent:
            self._root = right_child
        elif node is node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

        # Update heights.
        self._update_height(node)
        self._update_height(right_child)

        return right_child

    def _rotate_right(self, node: _AVLNode):
        # Perform right rotation.
        left_child = node.left
        node.left = left_child.right
        if left_child.right:
            left_child.right.parent = node
        left_child.parent = node.parent
        if not node.parent:
            self._root = left_child
        elif node is node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

        # Update heights.
        self._update_height(node)
        self._update_height(left_child)

        return left_child

