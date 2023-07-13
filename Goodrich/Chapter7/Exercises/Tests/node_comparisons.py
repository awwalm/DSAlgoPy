import sys
from Goodrich.Chapter7.Exercises.Utility.utils import *

l, m = SinglyLinkedList(1), SinglyLinkedList(1)
populate_nodes(l, 10)
populate_nodes(m, 10)
print(l.head is m.head)             # False
print(id(l.head) == id(l.head))     # True
