"""Tests for the proper doubly linked list class."""

from Goodrich.Chapter7.Exercises.Utility.utils import *


# Initialize and populate a doubly linked list.
l = SinglyLinkedList(1.25)
populate_nodes(l, 10)
print_nodes(l)

# Insert 4.75 and 5.75 before and after 5.25, respectively.
c = l.head
while c is not None:
    if c.element == 5.25:
        l.insert_before(4.75, c)
        l.insert_after(5.75, c)
        break
    c = c.next
print_nodes(l)

# Insert 0.25 before head node.
l.insert_before(0.25, l.head)
print_nodes(l)
