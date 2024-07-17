"""Hybrid (dual tree/array-based) Max-Heap implementation."""
from typing import Generic, TypeVar, List, Tuple
from Goodrich.Chapter13.GreedyTextCompression.utils import print_tree

K = TypeVar('K')
V = TypeVar('V')
class MaxHeap(Generic[K, V]):
    """
    A binary tree such that the value of the root is greater than
    or equal to the values of all subtrees rooted under it; recursively.

    + insert(k,v)
    + remove_max()
    + get_tree(node)
    - _structurize(keys,index,parent)
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
        self._data: List[Tuple[K, V]] = []
        self._size = len(self._data)

    def __len__(self):
        return self._size

    def _structurize(self, keys: list[tuple], index: int, parent):
        if index < len(keys):
            keyval = keys[index]
            node = self.Node(key=keyval[0], value=keyval[1], parent=parent)
            node.left = self._structurize(keys, 2 * index + 1, node)
            node.right = self._structurize(keys, 2 * index + 2, node)
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
        tree = self._structurize(self._data, 0, None)
        return tree

    def get_max(self):
        """Return but do not remove root of the heap."""
        return self._data[0]

    def insert(self, k: K, v: V):
        self._data.append((k, v))
        if self._size == 0:
            pass
        else:
            # SIFT-UP ROUTINE [O(log n) time]
            child = len(self._data) - 1
            while child > 0:
                parent = child // 2
                if self._data[parent][0] < self._data[child][0]:
                    temp = self._data[parent]
                    self._data[parent] = self._data[child]
                    self._data[child] = temp
                child = parent
        self._size += 1

    def remove_max(self):
        """
        Let h be a heap of tuples with keys = 64 51 31 18 29 2
        and corresponding indices as values:
        h = [(64,0), (51,1), (31,2), (18,3), (29,4), (2,5)]
        For every left child L, and right child R of every subsequent root node,
        we define `COI(index)` as the `Child of Index` function that maps
        valid indices to the left and right children when both/either are valid:
        L = ((parent_index + 1) * 2) - 1
        R = ((parent_index + 1) * 2)
        COI(i) = (L=NULL, R=NULL)  # Base case (singleton or empty heap)
        COI(0) = (L=1, R=2)
        COI(1) = (L=3, R=4)
        COI(2) = (L=5, R=NULL)
        """
        removed = self._data[0]
        self._data[0] = self._data[self._size-1]
        self._data.pop()
        self._size -= 1

        # SIFT-DOWN ROUTINE
        parent = 0
        rchild = (parent + 1) * 2
        lchild = rchild - 1
        while lchild < self._size:
            greater_child = rchild
            if rchild >= self._size:
                greater_child = lchild
            else:
                if self._data[lchild][0] >= self._data[rchild][0]:
                    greater_child = lchild
            if self._data[parent][0] < self._data[greater_child][0]:
                temp = self._data[parent]
                self._data[parent] = self._data[greater_child]
                self._data[greater_child] = temp
            parent += 1
            rchild = (parent + 1) * 2
            lchild = rchild - 1

        return removed



if __name__ == "__main__":
    A = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    B = [4, 8, 15, 16, 23, 42]
    C = [23, 34, 78, -1, 6, 90, 343, 5]
    D = [1, 5, 18, 5, 6, 1, 20]
    for data in A, B, C, D:
        heap = MaxHeap()
        for d in data: heap.insert(d,d)
        heap_tree = heap.get_tree()
        print([n.key for n in heap.bfs(heap_tree)])
        print_tree(heap_tree)
        print()
        for _ in range(len(data)):
            print(heap.remove_max())
        print()
