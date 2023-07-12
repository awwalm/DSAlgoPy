"""R-7.4: Describe in detail how to swap two nodes x and y (and not just their contents)
in a singly linked list L given references only to x and y.
Repeat this exercise for the case when L is a doubly linked list.
Which algorithm takes more time?.
"""
from Goodrich.Chapter7.Exercises.Utility.utils import *


# Iteration needed to find prev nodes - O(n) worst case.
def swap_nodes_singly(L, x, y):
    """:type L: SinglyLinkedList
       :type x: SinglyLinkedList._Node
       :type y: SinglyLinkedList._Node"""
    assert len(L) > 1, "Can't swap singleton node with self"
    xnext = x.next
    ynext = y.next
    xprev = yprev = None
    cur = L.head
    while cur is not None:
        if cur.next == x:
            xprev = cur
        elif cur.next == y:
            yprev = cur
        cur = cur.next
    if yprev is not None:
        yprev.next = x
        x.next = ynext
    if xprev is not None:
        xprev.next = y
        y.next = xnext


# Faster than its singly counterpart - prev nodes are already known, so O(1) time needed.
def swap_nodes_doubly(L, x, y):
    """:type L: DoublyLinkedList
       :type x: DoublyLinkedList._Node
       :type y: DoublyLinkedList._Node"""
    assert len(L) > 1, "Can't swap singleton node with self"
    xnext = x.next
    ynext = y.next
    xprev = x.prev
    yprev = y.prev
    if yprev is not None:
        yprev.next = x
        x.next = ynext
    if xprev is not None:
        xprev.next = y
        y.next = xnext


# Singly linked list node swap test.
l = SinglyLinkedList(1)
populate_nodes(l, 10)
nodex = nodey = None
curnode = l.head
while curnode is not None:
    if curnode.element == 2:
        nodex = curnode
    if curnode.element == 9:
        nodey = curnode
    curnode = curnode.next
swap_nodes_singly(l, nodex, nodey)
print_nodes(l)

# Doubly linked list node swap test.
l = DoublyLinkedList(1)
populate_nodes(l, 10)
nodex = nodey = None
curnode = l.head()
while curnode is not None:
    if curnode.element == 2:
        nodex = curnode
    if curnode.element == 9:
        nodey = curnode
    curnode = curnode.next
swap_nodes_doubly(l, nodex, nodey)
print_nodes(l)
