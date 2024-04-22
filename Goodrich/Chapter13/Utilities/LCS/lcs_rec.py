"""
Longest Common Subsequence solution using:

- Naive recursion; LCS(A, B)
- Inbuilt caching; LCSCACHE(A, B)
- Hashmap memoization; LCSMEMO(A, B)
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


def LCSMEMO(A: str, B: str, j: int, k: int, memotab: defaultdict):
    if memotab[(j, k)] == "N/A":
        pass
    else:
        return memotab[(j, k)]
    if (j == len(A)) or (k == len(B)):
        memotab[(j, k)] = 0
        return 0
    elif A[j] == B[k]:
        memotab[(j, k)] = 1 + LCSMEMO(A, B, j + 1, k + 1, memotab)
        return memotab[(j, k)]
    else:
        memotab[(j, k)] = max(
            LCSMEMO(A, B, j + 1, k, memotab), LCSMEMO(A, B, j, k + 1, memotab)
        )
        return memotab[(j, k)]



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
    ]

    for p in pairs:
        print(f"S1,S2 = {p}")

        t1 = time.perf_counter()
        sol = LCS(p[0], p[1], 0, 0)
        t2 = time.perf_counter()
        print(f"Time taken [LCS no cache] = {t2-t1:.10f}s")

        t1 = time.perf_counter()
        sol2 = LCSCACHE(p[0], p[1], 0, 0)
        t2 = time.perf_counter()
        print(f"Time taken [LCS with cache] = {t2 - t1:.10f}s")

        tab_ = defaultdict(lambda : "N/A")
        t1 = time.perf_counter()
        sol3 = LCSMEMO(p[0], p[1], 0, 0, tab_)
        t2 = time.perf_counter()
        print(f"Time taken [with memoization] = {t2 - t1:.10f}s")

        print(f"LCS no cache solution = {sol}")
        print(f"LCS cache solution = {sol2}")
        print(f"LCS memoization solution = {sol3}")
        # for key, val in zip(tab_.keys(), tab_.values()): print(f"{key} : {val}")
        print()
