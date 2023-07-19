"""R-7.11: Implement a function, with calling syntax ``max(L)``, that returns the maximum element
 from a ``PositionalList`` instance ``L`` containing comparable elements."""
import random

from Goodrich.Chapter7.positional_list import PositionalList


def Max(L: PositionalList):
    m = 0
    q = L.after(L.first())
    for p in L:
        if (p > q.element()) and (p > m) and (q is not None):
            m = p
            q = L.after(q)
    return m


# Instantiate doubly linked list and populate incrementally from 1 to 10.
dbll = PositionalList()
# noinspection PyProtectedMember
cur = dbll._header
for i in range(1, 11):
    # noinspection PyProtectedMember
    dbll._insert_between(i, cur, dbll._trailer)
    cur = cur.next

# Get max item.
print(Max(dbll))

# Also: PositionalList class already defines an iterable generator, simply call inbuilt max function.
print(max(dbll))

# Let's try that again with numbers from 1 to 10.
dbll = PositionalList()
# noinspection PyProtectedMember
cur = dbll._header
for i in random.sample(range(1, 11), 10):
    # noinspection PyProtectedMember
    dbll._insert_between(i, cur, dbll._trailer)
    cur = cur.next
print(Max(dbll))
print(max(dbll))
