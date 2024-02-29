"""Code Fragment 12.6: In-place quick-sort for a Python list S."""

def inplace_quick_sort(S, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
    if a >= b: return                               # Range is trivially sorted
    pivot = S[b]                                    # Last element of range is pivot
    left = a                                        # Will scan rightward
    right = b-1                                     # Will scan leftward

    while left <= right:
        # Scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        # Scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:                           # Scans did not strictly cross
            S[left], S[right] = S[right], S[left]   # Swap values
            left, right = left + 1, right - 1       # Shrink range

    # Put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)
