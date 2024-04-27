"""
Longest Common Subsequence solution using:

- Naive recursion; LCS(A, B, j, k)
- Inbuilt caching; LCSCACHE(A, B, j, k)
- Hashmap memoization; LCSMEMO(A, B, j, k, L)
- Buttom-up hashmap memoization; LCSBU(A, B, j, k, L)  {Surprisingly faster than top-down, on average}
"""

from collections import defaultdict
from functools import cache


def LCS(A, B, j: int, k: int):
    if (j == len(A)) or (k == len(B)):
        return 0
    elif A[j] == B[k]:
        return 1 + LCS(A, B, j+1, k+1)
    else:
        return max(LCS(A, B, j+1, k), LCS(A, B, j, k+1))


@cache
def LCSCACHE(A, B, j: int, k: int):
    if (j == len(A)) or (k == len(B)):
        return 0
    elif A[j] == B[k]:
        return 1 + LCS(A, B, j+1, k+1)
    else:
        return max(LCS(A, B, j+1, k), LCS(A, B, j, k+1))


def LCSMEMO(A: str, B: str, j: int, k: int, memo: defaultdict):
    if memo[(j, k)] == "N/A":
        pass
    else:
        return memo[(j, k)]
    if (j == len(A)) or (k == len(B)):
        memo[(j, k)] = 0
        return 0
    elif A[j] == B[k]:
        memo[(j, k)] = 1 + LCSMEMO(A, B, j + 1, k + 1, memo)
        return memo[(j, k)]
    else:
        memo[(j, k)] = max(
            LCSMEMO(A, B, j + 1, k, memo), LCSMEMO(A, B, j, k + 1, memo)
        )
        return memo[(j, k)]


def LCSBU(A: str, B: str, j: int, k: int, memo: defaultdict):
    if memo[(j,k)] == "N/A":
        pass
    else:
        return memo[(j,k)]
    if (j < 0) or (k < 0):
        memo[(j,k)] = 0
        return 0
    elif A[j] == B[k]:
        memo[(j,k)] = 1 + LCSBU(A, B, j-1, k-1, memo)
        return memo[(j,k)]
    else:
        memo[(j,k)] = max(
            LCSBU(A, B, j-1, k, memo), LCSBU(A, B, j, k-1, memo)
        )
        return memo[(j,k)]
