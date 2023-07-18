"""C-7.28 Describe a fast recursive algorithm for reversing a singly linked list.

Consider a disassembler algorithm that collects a copy of the current node,
then splits and processes it in isolation. Two MAJOR events must occur:

* The node current node points to must be saved temporarily.
* The next pointer of current node is then set to the previous node before it.

"""
from Goodrich.Chapter7.Exercises.Utility.utils import *


# This was surprisingly harder than I thought (https://www.geeksforgeeks.org/reverse-a-linked-list/)
def reverse(L: SinglyLinkedList, curnode, prevnode=None):
    """:type L: SinglyLinkedList
    :type curnode: SinglyLinkedList._Node | None
    :type prevnode: SinglyLinkedList._Node | None
    """
    if curnode is not None:
        nextnode = curnode.next
        curnode.next = prevnode
        prevnode = curnode
        curnode = nextnode
        return reverse(L, curnode, prevnode)
    else:
        L._header = prevnode


# Initialize and populate a singly linked list.
l = SinglyLinkedList(1)
populate_nodes(l, 9)
print_nodes(l)

reverse(l, l.head)
print_nodes(l)
