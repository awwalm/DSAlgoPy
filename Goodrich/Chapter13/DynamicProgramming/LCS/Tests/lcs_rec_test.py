"""Tests for recursive Longest Common Subsequence solution."""

from Goodrich.Chapter13.DynamicProgramming.LCS.lcs_rec import *

pairs = [
        ("ABCBDAB", "BDCAB"),               # BDAB (n=4)
        ("GTTCCTAATA", "CGATAATTGAGA"),     # GTTTAA (6)
        ("GTTCCTAAT", "CGATAATTGAG"),       # GTTTA (5)
        ("12345", "23415"),                 # 2345 (4)
        ("123", "1323"),                    # 123 (3)
        ("126548", "216544"),               # 2654 (4)
        ("AGGTAB", "GXTXAYB"),              # GTAB (4)
        ("BD", "ABCD"),                     # BD (2)
        ("ABCDGH", "AEDFHR"),               # ADH (3)
        ("ABCDE", "ACE"),                   # ACE (3)
        ("hofubmnylkra", "pqhgxgdofcvmr"),  # hofmr (5)
        ("oxcpqrsvwf", "shmtulqrypy"),      # qr (2)"
        ("ABC", "DEF"),                     # ∅ (0)
        ("stone", "longest"),               # one (3)
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
