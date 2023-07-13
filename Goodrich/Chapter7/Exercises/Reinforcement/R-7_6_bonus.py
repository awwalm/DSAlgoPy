"""A Bonus Concept to R-7.6: Suppose that x and y are references to nodes of circularly linked lists,
although not necessarily the same list. Describe a fast algorithm for telling
if x and y belong to  ̶t̶h̶e̶ ̶s̶a̶m̶e̶ an identical list."""
from Goodrich.Chapter7.Exercises.Utility.utils import *


def from_identical_list(x, y):
    """:type x: CircularSinglyLinkedList._Node
       :type y: CircularSinglyLinkedList._Node"""
    xhead = yhead = None
    while (x.element, y.element) != (None, None):
        if x.element == y.element:
            xhead, yhead = x, y
            break
        elif x.next == x:
            return False
        x = x.next
    while (x.element == y.element) and (y.next.element == x.next.element):
        if (x.next.element == xhead.element) and (y.next.element == yhead.element):
            return True
        x = x.next
        y = y.next
    return False


# Instantiate two circular linked lists with head elements = 1.
l, m = CircularSinglyLinkedList(1), CircularSinglyLinkedList(1)

# Populate each linked list node until a maximum node element of 10.
populate_nodes(l, 10)
populate_nodes(m, 10)

# This should return True.
print(from_identical_list(l.head.next, m.head))

# Re-instantiating 1 with fewer values/nodes should return False.
l = CircularSinglyLinkedList(1)
populate_nodes(l, 7)
print(from_identical_list(l.head.next, m.head.next))
