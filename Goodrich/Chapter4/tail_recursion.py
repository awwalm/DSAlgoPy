"""Some forms of recursion can be eliminated without any use of axillary memory.
A notable such form is known as tail recursion. A recursion is a tail recursion if
any recursive call that is made from one context is the very last operation in that context,
with the return value of the recursive call (if any) immediately returned by the enclosing recursion.
"""


def binary_search_iterative(data, target):
    """Return ``True`` if target is found in the given Python list."""
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:                             # Found a match.
            return True
        elif target < data[mid]:
            high = mid - 1                                  # Only consider values left of mid.
        else:
            low = mid + 1                                   # Only consider values right of mid.
    return False                                            # Loop ended without success.


def reverse_iterative(S):
    """Reverse elements in sequence S."""
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]       # Swap first and last.
        start, stop = start + 1, stop - 1                   # Narrow the range.
