"""Code Fragment 12.4: An implementation of the nonrecursive merge-sort algorithm."""
import math


def merge(src, result, start, inc):
    """Merge src[start:start+inc] and src[start+inc:start+2*inc] into result."""

    end1 = start+inc                        # Boundary for run 1
    end2 = min(start+2*inc, len(src))       # Boundary for run 2
    x, y, z = start, start+inc, start       # Index into run 1, run 2, result

    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x]; x+= 1       # Copy from run 1 and increment x
        else:
            result[z] = src[y]; y += 1      # Copy from run 2 and increment y
        z += 1                              # Increment z to reflect new result

    if x < end1:
        result[z:end2] = src[x:end1]        # Copy remainder of run 1 to output
    elif y < end2:
        result[z:end2] = src[y:end2]        # Copy remainder of run 2 to output

def merge_sort(S):
    """Sort the elememts of Python list S using the merge sort algorithm."""
    n = len(S)
    logn = math.ceil(math.log2(n))
    src, dest = S, [None] * n               # Make temporary storage for dest
    for i in (2**k for k in range(logn)):   # Pass i creates all runs of length 2i
        for j in range(0, n, 2*i):          # Each pass merges two length i runs
            merge(src, dest, j, i)
        src, dest = dest, src               # Reverse roles of lists
    if S is not src:
        S[0:n] = src[0:n]                   # Additional copy to get results to S
