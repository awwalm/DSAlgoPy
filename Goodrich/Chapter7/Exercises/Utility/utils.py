"""Singly and doubly linked list utilities. Let's abide by DRY principles!
With doubly linked lists being a subtype of singly linked lists,
all functions here are compatible with both, with precedence given to singly linked lists.
"""

from typing import Union
from Goodrich.Chapter7.Exercises.Utility.proper_singly_linked_list import SinglyLinkedList
from Goodrich.Chapter7.Exercises.Utility.proper_doubly_linked_list import DoublyLinkedList
from Goodrich.Chapter7.Exercises.Utility.circular_singly_linked_list import CircularSinglyLinkedList


def print_nodes(L: Union[SinglyLinkedList, DoublyLinkedList, CircularSinglyLinkedList]):
    try:
        h = cur = L.head()
    except TypeError:
        h = cur = L.head
    while cur is not None:
        print(cur.element)
        if cur.next == h:
            break
        cur = cur.next


def populate_nodes(L: Union[SinglyLinkedList, DoublyLinkedList, CircularSinglyLinkedList], limit: int):
    try:
        cur = L.head()
    except TypeError:
        cur = L.head
    assert cur.element < limit, "limit must be greater than head value"
    while cur is not None:
        L.insert_after(cur.element + 1, cur)
        if cur.element >= limit:
            break
        cur = cur.next
