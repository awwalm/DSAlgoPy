"""
Code Fragment 13.3: An implementation of the KMP pattern-matching algorithm.
The compute kmp fail utility function is given in Code Fragment 13.4.

Code Fragment 13.4: An implementation of the compute kmp fail utility
in support of the KMP pattern-matching algorithm.
Note how the algorithm uses the previous values of the failure function
to efficiently compute new values.
"""


def find_kmp(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)               # Introduce convenient notations
    if m == 0: return 0                 # Trivial search for empty string
    fail = compute_kmp_fail(P)          # Rely on utility to precompute
    j = 0                               # Index into text
    k = 0                               # Index into pattern
    while j < n:
        if T[j] == P[k]:                # P[0:1+k] matched thus far
            if k == m - 1:              # Match is complete
                return j - m + 1
            j += 1                      # Try to extend match
            k += 1
        elif k > 0:
            k = fail[k-1]               # Reuse suffix of P[0:k]
        else:
            j += 1
    return -1                           # Reached end without match


def compute_kmp_fail(P):
    """Utility that computes and returns KMP 'fail' list."""
    m = len(P)
    fail = [0] * m                      # By default, presume overlap of 0 everywhere
    j = 1
    k = 0
    while j < m:                        # Compute 𝒇(𝒋) during this pass, if nonzero
        if P[j] == P[k]:                # k + 1 characters match thus far
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:                     # k follows a matching prefix
            k = fail[k-1]
        else:                           # No match found starting at j
            j += 1
    return fail
