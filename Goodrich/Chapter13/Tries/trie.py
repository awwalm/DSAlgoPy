"""A basic Trie ADT."""

from typing import List, Union
from collections import OrderedDict


class Trie:
    """Basic Trie ADT with only insertion and search implemented."""

    class Node:
        def __init__(self, value, parent):
            self.value = value
            self.parent = parent
            self.terminal = False
            self.children: List[Trie.Node] = list()
            self.fast_child_access = OrderedDict()

    def __init__(self):
        self._size = 0
        self._char_count = 0
        self._root = Trie.Node(str(), None)

    def __len__(self):
        return self._size

    def count(self):
        return self._char_count

    def build(self, S: List[str]):
        self._char_count = sum(len(X) for X in S)
        cur = self._root
        for X in S:
            for x in X:
                if cur.fast_child_access.get(x):            # If character/letter exists...
                    cur = cur.fast_child_access.get(x)      # Consider a reuse
                else:                                       # Otherwise, create new branch
                    cur.children.append(Trie.Node(x, cur))
                    cur.fast_child_access[x] = Trie.Node(x, cur)
                    cur = cur.fast_child_access.get(x)
            cur.terminal = True                             # Set as terminal for partial matching
            cur = self._root
        self._size = sum(len(l) for l in self.bfs())
        return self._root

    def find(self, X):
        cur = self._root
        check: Union[Trie.Node, None] = None
        for x in X:
            check = cur.fast_child_access.get(x)
            if check is not None and check.value == x:
                cur = check                                 # Character match; onto next level
            else:                                           # Mismatch! Return false
                return False
        if check and len(check.children) == 0:              # Search terminated at leaf node
            return True
        else:                                               # Search terminated at internal node
            return cur.terminal                             # Check if this is a terminal node

    def bfs(self):
        this_level = [self._root]
        levels = []
        next_level = []
        while len(this_level) > 0:
            levels.append([n.value for n in this_level])
            for n in this_level:
                for eachN in n.fast_child_access.keys():
                    next_level.append(n.fast_child_access[eachN])
            this_level = next_level
            next_level = []
        return levels



def test_trie(S, BS):
    t = Trie()
    t.build(S)
    print(f"\n\nGood strings = {S}\nBad strings = {BS}")
    print(f"Trie size (nodes): {len(t)}")
    print(f"Trie count (total characters): {t.count()}")

    # Array representation of Compressed Trie
    print(f"Trie levels:")
    for i in [L for L in t.bfs()]:
        print(i)
    print()

    # Successful searches for strings in Compressed Trie
    for s in S:
        print(f"`{s}` in Trie: {t.find(s)}")
    print()

    # Unsuccessful searches for strings not in Compressed Trie
    for bs in BS:
        print(f"`{bs}` in Trie: {t.find(bs)} ")


if __name__ == "__main__":
    wiki_trie_data = ["test", "toaster", "toasting", "slow", "slowly"]
    strings1 = ["bear", "bell", "bid", "bull", "buy", "sell", "stock", "stop"]
    bad_strings = ["bo", "book", "animal", "bul", "bulls", "selling", "stoz", "bin", "sto"]
    strings2 = ["see", "bear", "sell", "stock", "see", "bull", "buy", "stock",
                "bid", "stock", "bid", "stock", "hear", "the", "bell", "stop"]
    test_trie(strings1, bad_strings)
    test_trie(strings2, bad_strings)
    test_trie(wiki_trie_data, bad_strings)
