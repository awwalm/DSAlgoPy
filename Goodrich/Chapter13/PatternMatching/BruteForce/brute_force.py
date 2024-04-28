# Code Fragment 13.1: An implementation of brute-force pattern-matching algorithm.
def find_brute(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)                       # introduce convenient notations
    for i in range(n-m+1):                      # try every potential starting index within T
        k = 0                                   # an index into pattern P
        while k < m and T[i + k] == P[k]:       # kth character of P matches
            k += 1
        if k == m:                              # if we reached the end of pattern
            return i                            # substring T[i:i+m] matches P
    return -1                                   # failed to find a match starting with any i
