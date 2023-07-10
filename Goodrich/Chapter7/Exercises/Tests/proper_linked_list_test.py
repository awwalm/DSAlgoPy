"""Tests for the proper doubly linked list class."""

from Goodrich.Chapter7.Exercises.proper_doubly_linked_list import DoublyLinkedList


def print_nodes(L: DoublyLinkedList):
    cur = L.head()
    while cur is not None:
        print(cur.element)
        cur = cur.next


def populate_nodes(L: DoublyLinkedList, limit: int):
    cur = L.head()
    assert cur.element < limit, "limit must be greater than head value"
    while cur is not None:
        L.insert_after(cur.element + 1, cur)
        cur = cur.next
        if cur.element >= limit:
            break


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
