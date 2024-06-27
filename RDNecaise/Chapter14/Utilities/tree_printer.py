"""Binary Tree printing heuristics."""

def print_pretty_tree(start_node):
    """From GitHub: https://github.com/zinchse/AVLTree"""
    space_symbol = r" "
    spaces_count = 4 * 2 ** start_node.height
    out_string = r""
    initial_spaces_string = space_symbol * spaces_count + "\n"
    if not start_node:
        return "Tree is empty"
    height = 2 ** start_node.height
    level = [start_node]

    while len([i for i in level if (not i is None)]) > 0:
        level_string = initial_spaces_string
        for i in range(len(level)):
            j = int((2 * i + 1) * spaces_count / (2 * len(level)))
            level_string = (level_string[:j]
                    + (str(level[i].value) if level[i] else space_symbol)
                    + level_string[j+1:])
        out_string += level_string

        # create next level
        level_next = []
        for i in level:
            level_next += ([i.left, i.right] if i else [None, None])
        # add connection to the next nodes
        for w in range(height - 1):
            level_string = initial_spaces_string
            for i in range(len(level)):
                if not level[i] is None:
                    shift = spaces_count // (2 * len(level))
                    j = (2 * i + 1) * shift
                    level_string = level_string[:j - w - 1] + (
                        '/' if level[i].left else
                        space_symbol) + level_string[j - w:]
                    level_string = level_string[:j + w + 1] + (
                        '\\' if level[i].right else
                        space_symbol) + level_string[j + w:]
            out_string += level_string
        height = height // 2
        level = level_next

    return out_string

def print_tree(root, show_height=False):
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
            valstr = str(f"{n[0].key}({n[0].height})") if show_height else str(n[0].key)
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
