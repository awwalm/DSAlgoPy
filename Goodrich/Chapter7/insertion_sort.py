"""Code Fragment 7.17: Python code for performing insertion-sort on a positional list."""
from Goodrich.Chapter7.positional_list import PositionalList


def insertion_sort(L: PositionalList):
    """Sort ``PositionalList`` of comparable elements into nondecreasing order."""
    if len(L) > 1:                          # Otherwise, no need to sort it.
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)         # Next item to place.
            value = pivot.element()
            if value > marker.element():    # Pivot is already sorted (CAREFUL if value is non-numeric!).
                marker = pivot              # Pivot becomes new marker.
            else:                           # Must relocate pivot.
                walk = marker               # Find leftmost item greater than value.
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)   # Reinsert value before walk.
