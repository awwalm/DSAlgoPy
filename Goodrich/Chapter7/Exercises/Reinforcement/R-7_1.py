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


l = SinglyLinkedList(1)
h = l.head

# Populate Linked List with values 1 to 10.
while h is not None:
    l.insert_after(h.element + 1, h)
    h = h.next
    if h.element == 10:
        break

# Print all node elements (should print 1 to 10)
h = l.head
while h is not None:
    print(h.element)
    h = h.next

# And now for my final trick...print 9!
n = find_second_to_last(l)
print(n.element)
