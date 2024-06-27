"""Binary Tree traversals."""

def inorder_traversal(node):
    if node.left:
        inorder_traversal(node.left)
    print(node.key)
    if node.right:
        inorder_traversal(node.right)

def bfs(level):
    if level.__len__() == 0:
        return
    next_level = []
    for node in level:
        if node:
            print(node.value)
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)
    del level
    bfs(next_level)