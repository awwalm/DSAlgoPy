"""A Compressed Trie ADT."""
# @FIXME: Had to allow partial matches to evaluate as successful search.
# @FIXME [cont'd]: Mild character duplication occurs at some nodes for overlapping strings.

from collections import OrderedDict
from typing import List, Union


class CompressedTrie:
    """
    Compresses a standard Trie using bottom-up compression from leaf nodes.
    Provides only insertion and search methods.
    """
    class Node:
        def __init__(self, keys, parent):
            self.keys: List = keys
            self.terminal = False
            self.compressed = OrderedDict()
            self.parent: Union[CompressedTrie.Node, None] = parent
            self.children: List[CompressedTrie.Node] = list()
            self.fast_child_access = OrderedDict()

    def __init__(self):
        self._size = 0
        self._char_count = 0
        self._root = CompressedTrie.Node(list(), None)
        self._leaves = list()

    def __len__(self):
        return self._size

    def count(self):
        return self._char_count

    # noinspection PyMethodMayBeStatic
    def _compress(self, leaves: List[Node]):
        for node in leaves:
            while len(node.keys) > 0:
                parent = node.parent
                if len(parent.fast_child_access) == 1:          # Node has only one child?
                    parent.keys.extend(node.keys)               # Then compress child with parent
                    parent.fast_child_access = OrderedDict()
                    parent.children = []
                    parent.compressed[node.keys[-1]] = node     # Register node as compressed
                    if len(node.children) > 0:
                        parent.children = node.children
                    if len(node.fast_child_access) > 0:
                        parent.fast_child_access = node.fast_child_access
                node = parent
        self._size = sum(len(l) for l in self.bfs())

    # noinspection PyMethodMayBeStatic
    def _add_empty_node(self, node):
        node.children.append(CompressedTrie.Node([str()], node))
        node.fast_child_access[str()] = CompressedTrie.Node([str()], node)

    def build(self, S: List[str]):
        self._char_count = sum(len(X) for X in S)
        cur = self._root
        if cur.terminal: self._add_empty_node(cur)      # Prevent false compression with empty node
        for X in S:
            for x in X:
                if cur.fast_child_access.get(x):        # If charater/letter exists...
                    if cur.terminal:
                        self._add_empty_node(cur)
                    cur = cur.fast_child_access.get(x)  # Consider a reuse
                    if cur.terminal:
                        self._add_empty_node(cur)
                else:                                   # Otherwise, create new branch
                    cur.children.append(CompressedTrie.Node([x], cur))
                    cur.fast_child_access[x] = CompressedTrie.Node([x], cur)
                    if cur.terminal:
                        self._add_empty_node(cur)
                    cur = cur.fast_child_access.get(x)
                    if cur.terminal:
                        self._add_empty_node(cur)
            cur.terminal = True
            self._leaves.append(cur)
            cur = self._root
        self._compress(self._leaves)                    # Begin bottom-up compression
        return self._root

    def find(self, X):
        cur = self._root
        x = 0
        check: Union[CompressedTrie.Node, None] = None
        while x < len(X):
            check = cur.fast_child_access.get(X[x])
            if check is not None:
                keylen = len(check.keys)
                if keylen > 1:
                    if list(X[x: x + keylen]) == check.keys:
                        cur = check             # Compressed string chain matches slice of X
                        x += keylen
                    else:                       # Mismatch; or not enough keys in slice of X
                        # return False
                        xslice = X[x: x + keylen]
                        if xslice in str().join(check.keys):
                            return check.compressed[xslice[-1]].terminal
                        else:
                            return False
                else:
                    if check.keys[0] == X[x]:
                        cur = check             # Character match; onto next level
                        x += 1
                    else:                       # Mismatch; different character found
                        return False
            else:                               # Mismatch; character not found
                return False
        if check and (len(check.children) == 0 or check.fast_child_access.get(str())):
            return True                         # Search terminated at leaf/terminal node
        else:                                   # Search terminated at internal node
            # return False
            return cur.terminal

    def bfs(self):
        this_level = [self._root]
        levels = []
        next_level = []
        while len(this_level) > 0:
            levels.append([n.keys for n in this_level])
            for n in this_level:
                for eachN in n.fast_child_access.keys():
                    next_level.append(n.fast_child_access[eachN])
            this_level = next_level
            next_level = []
        return levels



def test_compressed_trie(S, BS):
    t = CompressedTrie()
    t.build(S)
    print(f"\n\nGood strings = {S}\nBad strings = {BS}")
    print(f"Compressed Trie size (nodes): {len(t)}")
    print(f"Compressed Trie count (total characters): {t.count()}")

    # Array representation of Compressed Trie
    print(f"Compressed Trie levels:")
    for i in [L for L in t.bfs()]:
        print(i)
    print()

    # Successful searches for strings in Compressed Trie
    for s in S:
        print(f"`{s}` in Trie: {t.find(s)}")
    print()

    # Unsuccessful or partial searches for strings in (or not in) Compressed Trie
    for bs in BS:
        print(f"`{bs}` in Trie: {t.find(bs)} ")


if __name__ == "__main__":
    wiki_trie_data = ["test", "toaster", "toasting", "slow", "slowly"]
    strings1 = ["bear", "bell", "bid", "bull", "buy", "sell", "stock", "stop"]
    bad_strings = ["bo", "book", "animal", "bul", "bulls", "selling", "stoz", "bin", "sto"]
    strings2 = ["see", "bear", "sell", "stock", "see", "bull", "buy", "stock",
                "bid", "stock", "bid", "stock", "hear", "the", "bell", "stop"]
    test_compressed_trie(strings1, bad_strings)
    test_compressed_trie(strings2, bad_strings)
    test_compressed_trie(wiki_trie_data, bad_strings)
