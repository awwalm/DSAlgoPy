"""C-7.38: There is a simple, but inefficient, algorithm, called bubble-sort, for sorting
a list L of n comparable elements. This algorithm scans the list n−1 times,
where, in each scan, the algorithm compares the current element with the
next one and swaps them if they are out of order. Implement a bubble sort
function that takes a positional list L as a parameter. What is the running
time of this algorithm, assuming the positional list is implemented with a
doubly linked list?"""

from Goodrich.Chapter7.positional_list import PositionalList

# @FIXME: Untested!
def bubble(plist: PositionalList):
    if 0 <= plist.__len__() <= 1: return
    for i in range(plist.__len__()):
        pos = plist.first()
        for j in range(plist.__len__()):
            next_pos = plist.after(pos)
            if next_pos.element() < pos.element():
                after_pos = next_pos.after(pos)
                plist.add_before(pos, next_pos.element())
                plist.add_after(pos, after_pos.element())
                pos = after_pos
