"""R-7.3: Describe a recursive algorithm that counts the number of nodes in a singly linked list.
"""
from Goodrich.Chapter7.Exercises.Utility.utils import *


def recursive_count(N, c=0):
    """:type N: SinglyLinkedList._Node
       :type c: int"""
    if N is not None:
        return recursive_count(N.next, c + 1)
    return c


l = SinglyLinkedList(1)
populate_nodes(l, 10)
print(recursive_count(l.head))
