"""A basic Trie ADT."""

from typing import List
from collections import OrderedDict


class Trie:

    class Node:
        def __init__(self, value, parent):
            self.value = value
            self.parent = parent
            self.children: List[Trie.Node] = list()
            self.fast_child_access = OrderedDict()

    def __init__(self):
        self._size = 0
        self._root = Trie.Node(str(), None)

    def __len__(self):
        return self._size

    def build(self, S: List[str]):
        self._size = sum(len(X) for X in S)
        cur = self._root
        for X in S:
            for x in X:
                if cur.fast_child_access.get(x):            # If charater/letter exists...
                    cur = cur.fast_child_access.get(x)      # Consider a reuse
                else:                                       # Otherwise, create new branch
                    cur.children.append(Trie.Node(x, cur))
                    cur.fast_child_access[x] = Trie.Node(x, cur)
                    cur = cur.fast_child_access.get(x)
            cur = self._root
        return self._root

    def find(self, X):
        cur = self._root
        check = None
        for x in X:
            check = cur.fast_child_access.get(x)
            if check is not None and check.value == x:
                # print(check.value)
                cur = check                                 # Character match; onto next level
            else:                                           # Mismatch! Return false
                return False
        if check and len(check.children) == 0:              # Search terminates at leaf node
            return True
        else:                                               # Search terminates at internal node
            return False

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


if __name__ == "__main__":
    t = Trie()
    strings = ["bear", "bell", "bid", "bull", "buy", "sell", "stock", "stop"]
    bad_strings = ["bo", "book", "animal", "bulls", "selling", "stoz", "bin", "sto"]
    root = t.build(strings)
    print(f"Good strings = {strings}\nBad strings = {bad_strings}")
    print(f"Trie size: {len(t)}")
    print(f"Trie levels:")
    for i in [L for L in t.bfs()]:
        print(i)                                        # Array representation of Trie
    print()
    for s in strings:
        print(f"`{s}` in Trie: {t.find(s)}")            # True
    print()
    for bs in bad_strings:
        print(f"`{bs}` in Trie: {t.find(bs)} ")         # False
