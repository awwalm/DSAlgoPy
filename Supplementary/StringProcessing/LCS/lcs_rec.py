"""
Longest Common Subsequence solution using:

- Naive recursion; LCS(A, B, j, k)
- Inbuilt caching; LCSCACHE(A, B, j, k)
- Hashmap memoization; LCSMEMO(A, B, j, k, L)
- Buttom-up hashmap memoization; LCSBU(A, B, j, k, L)

Buttom-up is surprisingly faster than top-down, on average.
"""
import time
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


if __name__ == "__main__":
    pairs = [
        ("ABCBDAB", "BDCAB"),  # BDAB (n=4)
        ("GTTCCTAATA", "CGATAATTGAGA"),  # GTTTAA (6)
        ("GTTCCTAAT", "CGATAATTGAG"),  # GTTTA (5)
        ("12345", "23415"),  # 2345 (4)
        ("123", "1323"),  # 123 (3)
        ("126548", "216544"),  # 2654 (4)
        ("AGGTAB", "GXTXAYB"),  # GTAB (4)
        ("BD", "ABCD"),  # BD (2)
        ("ABCDGH", "AEDFHR"),  # ADH (3)
        ("ABCDE", "ACE"),  # ACE (3)
        ("hofubmnylkra", "pqhgxgdofcvmr"),  # hofmr (5)
        ("oxcpqrsvwf", "shmtulqrypy"),  # qr (2)"
        ("ABC", "DEF"),  # ∅ (0)
        ("stone", "longest"),  # one (3)
    ]

    for p in pairs:
        print(f"S1,S2 = {p}")

        t1 = time.perf_counter()
        sol = LCS(p[0], p[1], 0, 0)
        t2 = time.perf_counter()
        print(f"Time taken [LCS no cache] = {t2 - t1:.10f}s")

        t1 = time.perf_counter()
        sol2 = LCSCACHE(p[0], p[1], 0, 0)
        t2 = time.perf_counter()
        print(f"Time taken [LCS with cache] = {t2 - t1:.10f}s")

        # tab_ = defaultdict(lambda : "N/A")
        t1 = time.perf_counter()
        sol3 = LCSMEMO(p[0], p[1], 0, 0, defaultdict(lambda: "N/A"))
        t2 = time.perf_counter()
        print(f"Time taken [memoized/top-down] = {t2 - t1:.10f}s")

        # tab2 = defaultdict(lambda: "N/A")
        t1 = time.perf_counter()
        sol4 = LCSBU(p[0], p[1], len(p[0]) - 1, len(p[1]) - 1, defaultdict(lambda: "N/A"))
        t2 = time.perf_counter()
        print(f"Time taken [memoized/buttom-up] = {t2 - t1:.10f}s")

        print(f"LCS no cache solution = {sol}")
        print(f"LCS cache solution = {sol2}")
        print(f"LCS memoization top-down = {sol3}")
        print(f"LCS memoized buttom-up = {sol4}")
        # for key, val in zip(tab_.keys(), tab_.values()): print(f"{key} : {val}")
        print()
