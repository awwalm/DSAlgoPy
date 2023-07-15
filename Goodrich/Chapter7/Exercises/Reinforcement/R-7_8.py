"""R-7.8: Describe a nonrecursive method for finding, by link hopping,
the middle node of a doubly linked list with header and trailer sentinels.
In the case of an even number of nodes, report the node slightly left of center as the “middle.”
(Note: This method must only use link hopping; it cannot use a counter.)
What is the running time of this method?"""
from Goodrich.Chapter7.doubly_linked_list import _DoublyLinkedBase


class DoublyLinkedList(_DoublyLinkedBase):
    """Compact ``DoublyLinkedList`` subclass of the base provided in the book."""
    def __init__(self):
        super().__init__()

    @property
    def head(self):
        return self._header.next

    @property
    def tail(self):
        return self._trailer.prev

    def insert_between(self, e, predecessor, successor):
        super()._insert_between(e, predecessor, successor)


# noinspection PyProtectedMember
def middle(L: DoublyLinkedList):
    """Evaluates the middle node of a doubly linked list via simultaneous link hopping.
    Executes in O(n/2) time, where n = number of nodes in ``L``.\n
    :rtype: DoublyLinkedList._Node
    """
    ch, ct = L.head, L.tail
    while ch is not L._trailer:
        ch = ch.next
        if ch == ct:
            return ch.prev
        ct = ct.prev


# Instantiate doubly linked list and populate incrementally from 1 to 10.
dbll = DoublyLinkedList()
# noinspection PyProtectedMember
cur = dbll._header
for i in range(1, 11):
    # noinspection PyProtectedMember
    dbll.insert_between(i, cur, dbll._trailer)
    cur = cur.next

# Print element of mid node, i.e. 5.
print(middle(dbll).element)

# Let's try that again with odd node counts.
cur = dbll.tail.prev
for i in range(len(dbll) + 1, 20):
    # noinspection PyProtectedMember
    dbll.insert_between(i, cur, dbll._trailer)
    cur = cur.next

# Print element of mid node, i.e. 9.
print(middle(dbll).element)
