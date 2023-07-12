"""Tests for the proper doubly linked list class."""

from Goodrich.Chapter7.Exercises.Utility.utils import *


# Initialize and populate a doubly linked list.
l = DoublyLinkedList(1.25)
populate_nodes(l, 10)
print_nodes(l)

# Insert 4.75 and 5.75 before and after 5.25, respectively.
c = l.head()
while c is not None:
    if c.element == 5.25:
        l.insert_before(4.75, c)
        l.insert_after(5.75, c)
        break
    c = c.next
print_nodes(l)

# Insert 0.25 before head node.
l.insert_before(0.25, l.head())
print_nodes(l)

# Delete the additional nodes above.
c = l.head()
while c is not None:
    if c.element == 5.25:
        l.delete_node(c.prev)
        l.delete_node(c.next)
        break
    c = c.next
print_nodes(l)

# Attempt to delete head node and print new head (should print 2.25).
c = l.head()
while c is not None:
    if c == l.head():
        l.delete_node(c)
        break
    c = c.next
print(l.head().element)

# One more trick: insert 2.5 before 3, and 9.5 after 9.
curnode = l.head()
while curnode is not None:
    if curnode.element == 3:
        l.insert_before(2.5, curnode)
    if curnode.element == 9:
        l.insert_after(9.5, curnode)
    curnode = curnode.next
print_nodes(l)
