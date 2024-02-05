"""Code Fragment 12.1: An implementation of the merge operation for Python’s arraybased list class.
Code Fragment 12.2: An implementation of the recursive merge-sort algorithm for Python’s
array-based list class (using the merge function defined in Code Fragment 12.1."""

def merge(S1, S2, S):
    """Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i+j < len(S):
        # If S2 is full or S1 is still vacant AND currnet item in same index of S1 is less than S2...
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]      # Copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]      # Copy jth element of S2 as next item of S
            j += 1

def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    if n < 2: return            # List already sorted

    # DIVIDE
    mid = n//2
    S1 = S[0:mid]               # Copy of first half
    S2 = S[mid:n]               # Copy of second half

    # CONQUER (with recursion)
    merge_sort(S1)              # Sort copy of first half
    merge_sort(S2)              # Sort copy of second half

    # MERGE (the results)
    merge(S1, S2, S)            # Merge sorted halves back into S
