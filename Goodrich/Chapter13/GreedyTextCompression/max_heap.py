"""Hybrid (dual tree/array-based) Max-Heap implementation."""
from typing import Union
# from RDNecaise.Chapter14.Utilities.utils import print_pretty_tree


class MaxHeap:
    """
    A binary tree such that the value of the root is greater than
    the values of all subtrees rooted under it; recursively.

    + insert(k,v)
    + remove_max()
    + structurize()
    """
    # Nested Binary Tree class ------------------------------------------
    class _BinTree:
        class _Node:
            def __init__(self, k, v, p):
                self._root: Union[MaxHeap._BinTree._Node, None] = None
                self.key = k
                self.value = v
                self.parent = p
                self.height = 0
                self.left = None
                self.right = None

        def __init__(self):
            self._root = None
            self._size = 0


    # Max-Heap methods --------------------------------------------------
    def __init__(self):
        self._data = []
        self._size = len(self._data)

    def insert(self, k, v):
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
        and values = <corresponding indices>;
        h = [(64,0), (51,1), (31,2), (18,3), (29,4), (2,5)];
        For every left child L, and right child R of every subsequent root node,
        we define `COI(index)` as the `Child of Index` function that maps
        a valid index to a left, and a right child when valid:
        L = ((index + 1) * 2) - 1
        R = ((index + 1) * 2)
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
        for _ in range(len(data)):
            print(heap.remove_max())
        print()
