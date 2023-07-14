"""R-7.6: Suppose that x and y are references to nodes of circularly linked lists,
although not necessarily the same list. Describe a fast algorithm for telling
if x and y belong to the same list."""
from Goodrich.Chapter7.Exercises.Utility.utils import *


def from_same_list(x, y):
    """:type x: CircularSinglyLinkedList._Node
       :type y: CircularSinglyLinkedList._Node

       See Also
       --------
       ``Goodrich.Chapter7.Exercises.R-7_6_bonus.from_identical_list``
    """
    xhead = x                                 # Assume x node as the head (since the list is circular).
    while (x, y) != (None, None):             # `while True` will also suffice (circularly linked nodes are never None).
        if (x == y) and (x.next == y.next):   # Once y node is encountered, and it shares the same next objects in memory.
            return True                       # This is only possible if they are from the exact same list.
        x = x.next                            # Otherwise, keep iterating.
        if x == xhead:                        # If we arrive at tail node, without encountering y...
            return False                      # Then x and y are from different lists.


# Instantiate two circular linked lists with head elements = 1.
l, m = CircularSinglyLinkedList(1), CircularSinglyLinkedList(1)

# Populate each linked list node incrementally until 10.
populate_nodes(l, 10)
populate_nodes(m, 10)

# These two comparisons should return False (l and m are different although identical).
print(from_same_list(l.head, m.head.next))
print(from_same_list(l.head, m.head))

# This should return True (while the nodes compared are different, they are from a common list).
print(from_same_list(l.head, l.head.next.next))
