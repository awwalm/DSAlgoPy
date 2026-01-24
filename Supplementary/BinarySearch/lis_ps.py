from __future__ import annotations
from bisect import bisect_left
from dataclasses import dataclass
from typing import List

def lis_ps(nums: List[int]):
    """
    Longest Increasing Subsequence algorithm using a Patience Sort intuition.
    See https://www.youtube.com/watch?v=WNJnsmOoTJs
    """

    @dataclass
    class Node:
        stack: List[int]
        top: int
        nxt: Node | None
        candidate: int

    bst: List[Node] = []  # Pseudo-BST (only search ops are logarithmic)
    n = len(nums)

    for i in range(n):
        ins_point = bisect_left(bst, nums[i], key=lambda obj: obj.top)
        if len(bst) == 0:
            bst.insert(ins_point, Node([nums[i]], nums[i], None, nums[i]))
        else:
            if ins_point < len(bst):
                if bst[ins_point].top > nums[i]:
                    bst[ins_point].stack.append(nums[i])
                    bst[ins_point].top = nums[i]
            else:   # Create a new pile, i.e. insert new BST Node, and add activate LIS candidate
                bst[ins_point-1].candidate = bst[ins_point-1].top
                new_node = Node([nums[i]], nums[i], None, nums[i])
                bst.insert(ins_point, new_node)
                bst[ins_point-1].nxt = new_node

    return [n.candidate for n in bst]   # <- Activated candidates are the guaranteed LIS
    # return [n.top for n in bst]       # <- Top of each stack won't always be the LIS


def test(inputs: List[List[int]]):
    for i in inputs:
        print(i, lis_ps(i), sep="\n")
        print()


if __name__ == '__main__':
    data = [
        [],
        [-12],
        [7, 7, 7, 7, 7, 7, 7],
        [3, 7, 5, 6, 4, 2, 10, 9, 8, 12, 1],
        [10, 22, 9, 33, 21, 50, 41, 60],
        [1, 2, 3, 4],
        [1, 3, 2, 4],
        [3, 10, 2, 1, 20],
        [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
        [5, 1, 6, 2, 7, 3, 8],
        [3, 7, 5, 6, 4, 2, 10, 9, 8, 12, 1, 0]
    ]
    test(data)
