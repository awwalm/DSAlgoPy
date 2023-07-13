"""R-7.5: Implement a function that counts the number of nodes in a circularly linked list."""
from Goodrich.Chapter7.Exercises.Utility.utils import *


def circular_recursive_count(L: CircularSinglyLinkedList, N, c=1):
    """:type L: CircularSinglyLinkedList
       :type N: CircularSinglyLinkedList._Node
       :type c: int"""
    if N.next is not L.head:
        return circular_recursive_count(L, N.next, c + 1)
    return c


# Initialize and populate a circular singly linked list.
l = CircularSinglyLinkedList(1)
populate_nodes(l, 9)
print(circular_recursive_count(l, l.head))
