"""When a function makes two recursive calls, we say that it uses binary recursion."""


def binary_sum(S, start, stop):
    """Return the sum of the numbers in implicit slice ``S[start:stop]``."""
    if start >= stop:               # Zero elements in slice.
        return 0
    elif start == stop-1:           # One element in slice.
        return S[start]
    else:                           # Two or more elements in slice
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
