"""R-7.1 Give an algorithm for finding the second-to-last node in a singly linked list
in which the last node is indicated by a next reference of None.
"""
from Goodrich.Chapter7.Exercises.Utility.utils import *


# The algorithm.
def find_second_to_last(L: Union[SinglyLinkedList, DoublyLinkedList]):
    cur = L.head
    while cur is not None and cur.next is not None:
        if cur.next.next is None:
            return cur
        cur = cur.next


# Create a new singly linked list with a node with element 1.
l = SinglyLinkedList(1)

# Populate Linked List with values 1 to 10.
populate_nodes(l, 10)

# Print all node elements (should print 1 to 10)
print_nodes(l)

# And now for my final trick...print 9!
n = find_second_to_last(l)
print(n.element)
