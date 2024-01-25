import random
from RDNecaise.Chapter14.avltree import AVLTree as AVLTreeA
from RDNecaise.Chapter14.avltree2 import AVLTree as AVLTreeB
from RDNecaise.Chapter14.avltree3 import AVLTree as AVLTreeC


def inorder_traversal2(node):
    if node.leftChild:
        inorder_traversal2(node.leftChild)
    print(node.key)
    if node.rightChild:
        inorder_traversal2(node.rightChild)

def inorder_traversal3(node):
    if node.left:
        inorder_traversal3(node.left)
    print(node.key)
    if node.right:
        inorder_traversal3(node.right)

def print_tree2(root):
    """From StackOverflow: https://stackoverflow.com/a/72497198/13488161"""
    def height(__node):
        return 1 + max(height(__node.leftChild), height(__node.rightChild)) if __node else -1
    nlevels = height(root)
    width = pow(2, nlevels + 1)
    q = [(root, 0, width, 'c')]
    levels = []
    while q:
        node, level, x, align = q.pop(0)
        if node:
            if len(levels) <= level:
                levels.append([])
            levels[level].append([node, level, x, align])
            seg = width // (pow(2, level + 1))
            q.append((node.leftChild, level + 1, x - seg, 'l'))
            q.append((node.rightChild, level + 1, x + seg, 'r'))
    for j, l in enumerate(levels):
        pre = 0
        preline = 0
        linestr = ''
        pstr = ''
        seg = width // (pow(2, j + 1))
        for n in l:
            valstr = str(f"{n[0].key}(h={n[0].height})")
            if n[3] == 'r':
                linestr += ' ' * (n[2] - preline - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
                preline = n[2]
            if n[3] == 'l':
                linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)
                preline = n[2] + seg + seg // 2
            pstr += ' ' * (n[2] - pre - len(valstr)) + valstr  # correct the potition acording to the number size
            pre = n[2]
        print(linestr)
        print(pstr)

def print_tree3(root):
    """From StackOverflow: https://stackoverflow.com/a/72497198/13488161"""
    def height(__node):
        return 1 + max(height(__node.left), height(__node.right)) if __node else -1
    nlevels = height(root)
    width = pow(2, nlevels + 1)
    q = [(root, 0, width, 'c')]
    levels = []
    while q:
        node, level, x, align = q.pop(0)
        if node:
            if len(levels) <= level:
                levels.append([])
            levels[level].append([node, level, x, align])
            seg = width // (pow(2, level + 1))
            q.append((node.left, level + 1, x - seg, 'l'))
            q.append((node.right, level + 1, x + seg, 'r'))
    for j, l in enumerate(levels):
        pre = 0
        preline = 0
        linestr = ''
        pstr = ''
        seg = width // (pow(2, j + 1))
        for n in l:
            valstr = str(f"{n[0].key}({n[0].height})")
            if n[3] == 'r':
                linestr += ' ' * (n[2] - preline - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
                preline = n[2]
            if n[3] == 'l':
                linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)
                preline = n[2] + seg + seg // 2
            pstr += ' ' * (n[2] - pre - len(valstr)) + valstr  # correct the potition acording to the number size
            pre = n[2]
        print(linestr)
        print(pstr)

def test1():
    tree = AVLTreeA()
    vals = [3,8,10,4,1,2,9,6,5,7,17,12,15,21,18,19,13,3,8,10,4,1,2]
    lim = random.randrange(15, 30)
    for i in random.sample(range(1, lim+1), lim): #vals:
        print(f"\ncurrent key/value: {i}")
        tree.insert(i, i)
        print_tree3(tree.root())
    print(f"5 in tree: {5 in tree}")
    print(f"15 in tree: {15 in tree}")
    inorder_traversal3(tree.root())

def test2():
    tree = AVLTreeB()
    vals = [3,8,10,4,1,2,9,6,5,7,17,12,15,21,18,19,13,3,8,10,4,1,2]
    lim = random.randrange(15, 30)
    for i in random.sample(range(1, lim+1), lim): #vals:
        print(f"\ncurrent key/value: {i}")
        root = tree.insert(i)
        # print_tree(tree.rootNode)
        print(tree)
    inorder_traversal2(tree.rootNode)

def test3():
    tree = AVLTreeC()
    vals = [3,8,10,4,1,2,9,6,5,7,17,12,15,21,18,19,13,3,8,10,4,1,2]
    lim = random.randrange(10, 16)
    for i in vals: # random.sample(range(1, lim+1), lim): #vals:
        print(f"\ncurrent key/value: {i}")
        tree.insert(i, i)
        print_tree3(tree.root())
    tree.delete(6)
    print("Key 6 deleted")
    print_tree3(tree.root())
    print(f"5 in tree: {5 in tree}")
    print(f"25 in tree: {25 in tree}")
    inorder_traversal3(tree.root())

test3()
