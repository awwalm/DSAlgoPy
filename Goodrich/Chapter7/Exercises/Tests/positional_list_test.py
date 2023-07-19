"""Tests for the Positional List class."""
from Goodrich.Chapter7.positional_list import PositionalList
import random

dbll = PositionalList()
# noinspection PyProtectedMember
cur = dbll._header
for i in random.sample(range(1, 11), 10):
    # noinspection PyProtectedMember
    dbll._insert_between(i, cur, dbll._trailer)
    cur = cur.next

print(dbll.max())                   # 10
print(max(dbll))                    # Also 10
print(dbll.find(5).element())       # Prints 5 once encountered
# print(dbll.find(11).element())    # ValueError - 11 not in list
print(dbll.recursive_find(          # 7
    7, dbll.first()).element())
# print(dbll.recursive_find(
#    17, dbll.first()).element())   # ValueError - 17 not in list

for i in dbll:
    print(i)

for i in reversed(dbll):
    print(i)
