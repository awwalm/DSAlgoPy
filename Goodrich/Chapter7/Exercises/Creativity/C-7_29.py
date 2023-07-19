"""C-7.29: Describe in detail an algorithm for reversing a singly linked list L
using only a constant amount of additional space and not using any recursion.
"""
from Goodrich.Chapter7.Exercises.Utility.utils import *


def reverse(L: SinglyLinkedList):
    curnode, prevnode = L.head, None
    while curnode is not None:
        nextnode = curnode.next
        curnode.next = prevnode
        prevnode = curnode
        curnode = nextnode
    L._header = prevnode


# Initialize and populate a singly linked list.
l = SinglyLinkedList(1)
populate_nodes(l, 9)
print_nodes(l)

reverse(l)
print_nodes(l)
