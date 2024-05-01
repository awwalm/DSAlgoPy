"""Utilities for Huffman Coding algorithm."""

def print_tree(root):
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
            valstr = str(f"{n[0].key}")
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
