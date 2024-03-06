from Goodrich.Chapter7.Exercises.Utility.utils import *

def reverse_list(L: SinglyLinkedList):
    cur = L.head
    prev = None
    while cur is not None:      # Shift two pointers incrementally
        after_cur = cur.next
        cur.next = prev
        prev = cur
        cur = after_cur
    L._header = prev



l = SinglyLinkedList(1)
populate_nodes(l, 9)
print_nodes(l)
reverse_list(l)
print_nodes(l)
