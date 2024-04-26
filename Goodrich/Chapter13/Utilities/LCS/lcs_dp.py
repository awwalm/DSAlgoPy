"""
Longest Common Subsequence solution using classic Dynamic Programming.
"""
import time


def BUILD_LCS(A: str, B: str, L: dict):
    n, m = len(A), len(B)
    for row in range(n+1): L[(row, 0)] = 0              # Fill first column with 0 to allow initialization
    for col in range(m+1): L[(0, col)] = 0              # Fill first row with 0 to allow initialization
    for k in range(1, m+1):                             # Column iteration [we calculate columns first]
        for j in range(1, n+1):                         # Row iteration
            if A[j-1] == B[k-1]:
                L[(j,k)] = 1 + L[(j-1,k-1)]
            else:
                L[(j,k)] = max(L[(j-1,k)], L[(j,k-1)])
    return L


def GET_LCS(A: str, B: str, L: dict):
    S = []
    n, m = len(A), len(B)
    while (n > 0) and (m > 0):
        if (L[(n, m)] > L[(n, m-1)]) or (L[(n, m)] != L[(n, m-1)]):
            S.append(m-1)
            n -= 1; m -= 1
        else:
            m -= 1
    return list(map(lambda f: B[f], reversed(S)))



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
        print(f"\nS1,S2 = {p}")

        t1 = time.perf_counter()
        tab = BUILD_LCS(p[0], p[1], dict())
        t2 = time.perf_counter()

        print(f"LCS = {GET_LCS(p[0], p[1], tab)}")
        print(f"LCS len = {tab[(len(p[0]), len(p[1]))]}")
        print(f"Time taken [LCS DP] = {t2-t1:.10f}s")

        # DP Table printing
        for c in range(len(p[1]) + 1):
            ri = []
            for r in range(len(p[0]) + 1):
                ri.append(tab[(r, c)])
            print(ri)
