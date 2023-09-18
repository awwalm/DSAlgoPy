from RDNecaise.Chapter13.bintreenode import _BinTreeNode


# Listing 13.2: Preorder traversal on a binary tree. - O(n)
def preorderTrav(subtree: _BinTreeNode):
    """1. Visit the node (subroot).
    2. Traverse the left subtree.
    3. Traverse the right subtree.
    """
    if subtree is not None:
        print(subtree.data)
        preorderTrav(subtree.left)
        preorderTrav(subtree.right)

# Listing 13.3: Inorder traversal on a binary tree. - O(n)
def inorderTrav(subtree: _BinTreeNode):
    """1. Traverse the left subtree (actually 1st left leaf node).
    2. Visit the node (subroot).
    3. Traverse the right subtree.
    """
    if subtree is not None:
        inorderTrav(subtree.left)
        print(subtree.data)
        inorderTrav(subtree.right)

# Listing 13.4: Postorder traversal on a binary tree (opposite of preorder).
def postorderTrav(subtree: _BinTreeNode):
    """1. Traverse the left subtree.
    2. Traverse the right subtree.
    3. Visit the node.
    """
    if subtree is not None:
        postorderTrav(subtree.left)
        postorderTrav(subtree.right)
        print(subtree.data)

