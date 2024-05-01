"""Hybrid (dual tree/array-based) Min-Heap implementation."""
from utils import print_tree


class MinHeap:
    """
    A binary tree such that the value of the root is less than or
    equal to the values of all subtrees rooted under it; recursively.

    + insert(k,v)
    + remove_max()
    + structurize(keys,index,parent)
    """

    class Node:
        def __init__(self, key, value, parent):
            self.key = key
            self.value = value
            self.parent = parent
            self.left = None
            self.right = None
            self.height = 0

    def __init__(self):
        self._data = []
        self._size = len(self._data)

    def __len__(self):
        return self._size

    def insert(self, k, v):
        self._data.append((k,v))
        self._size += 1
        rchild = self._size - 1
        lchild = rchild - 1

        # SIFT-UP LOGIC
        while rchild > 0:
            child = lchild
            if lchild < 0:
                child = rchild
            else:
                if self._data[rchild][0] < self._data[lchild][0]:
                    child = rchild
            parent = child // 2
            if self._data[child][0] < self._data[parent][0]:
                temp = self._data[child]
                self._data[child] = self._data[parent]
                self._data[parent] = temp
            rchild = parent
            lchild = rchild - 1

    def remove_min(self):
        removed = self._data[0]
        self._data[0] = self._data[self._size - 1]
        self._data.pop()
        self._size -= 1

        # SIFT-DOWN LOGIC
        parent = 0
        rchild = (parent + 1) * 2
        lchild = rchild - 1
        while lchild < self._size:
            lesserchild = rchild
            if rchild >= self._size:
                lesserchild = lchild
            else:
                if self._data[lchild][0] <= self._data[rchild][0]:
                    lesserchild = lchild
            if self._data[lesserchild][0] < self._data[parent][0]:
                temp = self._data[lesserchild]
                self._data[lesserchild] = self._data[parent]
                self._data[parent] = temp
            parent += 1
            rchild = (parent + 1) * 2
            lchild = rchild - 1

        return removed


    def structurize(self, keys: list[tuple], index: int, parent):
        if index < len(keys):
            keyval = keys[index]
            node = self.Node(key=keyval[0], value=keyval[1], parent=parent)
            node.left = self.structurize(keys, 2 * index + 1, node)
            node.right = self.structurize(keys, 2 * index + 2, node)
            return node

    # noinspection PyMethodMayBeStatic
    def bfs(self, start: Node):
        this_level = [start]
        next_level = []
        nodes = []
        while len(this_level) > 0:
            for node in this_level:
                if node: nodes.append(node)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            this_level = next_level
            next_level = []
        return nodes

    def get_tree(self):
        tree = self.structurize(self._data, 0, None)
        return tree



if __name__ == "__main__":
    A = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    B = [4, 8, 15, 16, 23, 42]
    C = [23, 34, 78, -1, 6, 90, 343, 5]
    D = [1, 5, 18, 5, 6, 1, 20]
    for data in A, B, C, D:
        heap = MinHeap()
        for d in data: heap.insert(d,d)
        heap_tree = heap.get_tree()
        print([n.key for n in heap.bfs(heap_tree)])
        print_tree(heap_tree)
        print()
        for _ in range(len(data)):
            print(heap.remove_min())
        print()
