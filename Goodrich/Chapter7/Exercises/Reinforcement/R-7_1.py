"""R-7.1 Give an algorithm for finding the second-to-last node in a singly linked list
in which the last node is indicated by a next reference of None.

ALGORITHM FindSecondToLast(L: LinkedList):
    cur = L.head
    while cur.next != None:
        return cur if cur.next is L.tail else pass
        cur = cur.next
"""
from Goodrich.Chapter7.Exercises.proper_singly_linked_list import SinglyLinkedList


def find_second_to_last(L: SinglyLinkedList):
    cur = L.head
    while cur is not None and cur.next is not None:
        if cur.next.next is None:
            return cur
        cur = cur.next


def print_nodes(L: SinglyLinkedList):
    cur = L.head
    while cur is not None:
        print(cur.element)
        cur = cur.next


def populate_nodes(L: SinglyLinkedList, limit: int):
    cur = L.head
    assert cur.element < limit, "limit must be greater than head value"
    while cur is not None:
        L.insert_after(cur.element + 1, cur)
        cur = cur.next
        if cur.element == limit:
            break


l = SinglyLinkedList(1)

# Populate Linked List with values 1 to 10.
populate_nodes(l, 10)

# Print all node elements (should print 1 to 10)
print_nodes(l)

# And now for my final trick...print 9!
n = find_second_to_last(l)
print(n.element)

# One more trick: insert 2.5 before 3, and 9.5 after 9.
curnode = l.head
while curnode is not None:
    if curnode.element == 3:
        l.insert_before(2.5, curnode)
    if curnode.element == 9:
        l.insert_after(9.5, curnode)
    curnode = curnode.next
print_nodes(l)
