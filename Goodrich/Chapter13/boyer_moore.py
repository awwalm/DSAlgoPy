"""Code Fragment 13.2: An implementation of the Boyer-Moore algorithm."""

def find_boyer_moore(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)               # Introduce convenient notations
    if m == 0: return 0                 # Trivial search for empty string
    last = { }                          # Build 'last' dictionary
    for k in range(m):
        last[ P[k] ] = k                # Later occurrence overwrites
    # Align end of pattern at index m-1 of text
    i = m - 1                           # An index into T
    k = m - 1                           # An index into P
    while i < n:
        if T[i] == P[k]:                # A matching character
            if k == 0:
                return i                # Pattern begins at index i of text
            else:
                i -= 1                  # Examine previous character
                k -= 1                  # of both T and P
        else:
            j = last.get(T[i], -1)      # Last(T[i]) is -1 if not found
            i += m - min(k, j+1)        # Case analysis for jump step
            k = m - 1                   # Restart at end of pattern
    return -1
