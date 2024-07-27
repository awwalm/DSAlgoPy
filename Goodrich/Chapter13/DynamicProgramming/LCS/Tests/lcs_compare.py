"""Comparison tests between textbook and custom Longest Common Subsequence solutions."""

from Supplementary.StringProcessing.LCS.lcs_rec import *
from Supplementary.StringProcessing.LCS.lcs_dp import *
from Goodrich.Chapter13.DynamicProgramming.LCS.lcs import *

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
    sol1 = LCSMEMO(p[0], p[1], 0, 0, defaultdict(lambda: "N/A"))
    t2 = time.perf_counter()
    print(f"Time taken [memoized/top-down] = {t2 - t1:.10f}s")

    t1 = time.perf_counter()
    sol2 = LCSBU(p[0], p[1], len(p[0]) - 1, len(p[1]) - 1, defaultdict(lambda: "N/A"))
    t2 = time.perf_counter()
    print(f"Time taken [memoized/buttom-up] = {t2 - t1:.10f}s")

    t1 = time.perf_counter()
    tab = BUILD_LCS(p[0], p[1], dict())
    t2 = time.perf_counter()
    print(f"Time taken [LCS DP] = {t2 - t1:.10f}s")

    t1 = time.perf_counter()
    tab2 = LCS(p[0], p[1])
    t2 = time.perf_counter()
    print(f"Time taken [LCS Textbook] = {t2 - t1:.10f}s")

    print(f"LCS = {GET_LCS(p[0], p[1], tab)}")
    print(f"LCS len = {tab[(len(p[0]), len(p[1]))]}")

    # DP table printing
    print("Hashmap DP table:")
    for r in range(len(p[0]) + 1):
        ri = []
        for c in range(len(p[1]) + 1):
            ri.append(tab[(r, c)])
        print(ri)

    print("Textbook DP Table:")
    for r in tab2: print(r)

    # for key, val in zip(tab_.keys(), tab_.values()): print(f"{key} : {val}")
    print()
