"""
Longest Common Subsequence solution using a custom
`Common Element Table` (CET) construction technique.
It complements the inadequacies of the Two-Pointer (TP) method
by recorrecting itself with the CET generated results.
The CET technique similarly complements its inadequacies with the TP results.
"""
from collections import deque


# Two-Pointer component
def TP_LCS(A: str, B: str):
    lcs1, lcs2 = [], []
    def scan_match(J, K, a, b, lcs):
        for j in range(J, len(a)):
            for k in range(K, len(b)):
                if a[j] == b[k]:
                    lcs.append(a[j])
                    return scan_match(j+1, k+1, a, b, lcs)
    scan_match(0, 0, A, B, lcs1)
    scan_match(0, 0, B, A, lcs2)
    return lcs1 if len(lcs1) > len(lcs2) else lcs2


# Common Element Tabulation component
def CET_LCS(A: str, B: str):
    CET : list[list | list] = [              # Common Element Table
        [j for j in range(len(A))], [deque() for _ in range(len(A))] ]
    PM : list[int] = []                     # Partial/Potential Matches

    for j in range(len(A)):                 # Construct CET with respect due to A
        for k in range(len(B)):             # Find all occurences of A[j] in B
            if A[j] == B[k]:
                CET[1][j].append(k)         # Enqueue all matches in bucket under A[j]

    pm = []                                 # PM cache
    for j in range(len(A)):
        if len(CET[1][j]) == 0:
            continue
        else:
            if len(pm) > 0:
                prev = pm[len(pm)-1]
                matched = None
                for m in CET[1][j]:
                    if m > prev:
                        pm.append(m)
                        matched = m
                        break
                if not matched:
                    if len(pm) > len(PM): PM = pm
                    pm = []
            else:
                m = CET[1][j].popleft()
                pm.append(m)
    if len(pm) > len(PM): PM = pm

    print(f"B indices of matches: {PM}")

    return [B[k] for k in PM]


if __name__ == "__main__":
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
            ("oxcpqrsvwf", "shmtulqrypy"),  # @TODO: Currently unable to detect subsequence "qr"
            ("ABC", "DEF"),  # ∅ (0)
        ]
        for p in pairs:
            print(f"LCS{p} = {max([TP_LCS(*p), CET_LCS(*p)], key=len)}\n")


