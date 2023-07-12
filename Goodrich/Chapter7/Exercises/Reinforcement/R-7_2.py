"""R-7.2: Describe a good algorithm for concatenating two singly linked lists L and M,
 given only references to the first node of each list, into a single list L`
 that contains all the nodes of L followed by all the nodes of M.
"""
from Goodrich.Chapter7.Exercises.Utility.utils import *


def concatenate_sll(L: SinglyLinkedList, M: SinglyLinkedList):
    L_ = L
    cur = L_.head
    while cur is not None:
        if cur.next is None:
            cur.next = M.head
            break
        cur = cur.next
    return L_


# Instantiate 2 singly linked lists.
l, m = SinglyLinkedList(1), SinglyLinkedList(6)
populate_nodes(l, 5)
populate_nodes(m, 10)
l_ = concatenate_sll(l, m)
print_nodes(l_)
