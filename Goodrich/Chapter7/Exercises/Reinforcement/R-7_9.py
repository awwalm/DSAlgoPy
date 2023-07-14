"""R-7.9: Give a fast algorithm for concatenating two doubly linked lists L and M,
 with header and trailer sentinel nodes, into a single list L_."""
from Goodrich.Chapter7.doubly_linked_list import _DoublyLinkedBase


# noinspection PyProtectedMember
def concatenate(L, M):
    """:type L: _DoublyLinkedBase
       :type M: _DoublyLinkedBase"""
    L_ = L
    L_._trailer.prev.next = M._header.next
    L_._trailer = M._trailer
    return L_
