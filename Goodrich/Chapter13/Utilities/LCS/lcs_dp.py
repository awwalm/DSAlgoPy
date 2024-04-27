"""Longest Common Subsequence solution using classic Dynamic Programming."""
import time


def BUILD_LCS(A: str, B: str, L: dict):
    n, m = len(A), len(B)
    for row in range(n+1): L[(row, 0)] = 0      # Initialize first column cells to 0
    for col in range(m+1): L[(0, col)] = 0      # Initialize first row cells to 0
    for k in range(1, m+1):                     # Fill columns first (left to right)
        for j in range(1, n+1):                 # Row iteration
            if A[j-1] == B[k-1]:
                L[(j,k)] = 1 + L[(j-1,k-1)]
            else:
                L[(j,k)] = max(L[(j-1,k)], L[(j,k-1)])
    return L


def GET_LCS(A: str, B: str, L: dict):
    S = []
    n, m = len(A), len(B)
    while L[(n,m)] > 0:
        if A[n-1] == B[m-1]:
            S.append(A[n-1])
            n -= 1; m -= 1
        elif L[(n-1, m)] >= L[(n, m-1)]:
            n -= 1
        else:
            m -= 1
    return str().join(reversed(S))


if __name__ == "__main__":
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
        print(f"\nS1,S2 = {p}")

        t1 = time.perf_counter()
        tab = BUILD_LCS(p[0], p[1], dict())
        t2 = time.perf_counter()

        print(f"LCS = {GET_LCS(p[0], p[1], tab)}")
        print(f"LCS len = {tab[(len(p[0]), len(p[1]))]}")
        print(f"Time taken [LCS DP] = {t2-t1:.10f}s")

        # DP table printing
        for r in range(len(p[0]) + 1):
            ri = []
            for c in range(len(p[1]) + 1):
                ri.append(tab[(r,c)])
            print(ri)
