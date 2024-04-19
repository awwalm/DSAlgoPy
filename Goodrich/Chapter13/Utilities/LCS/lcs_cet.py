"""
Longest Common Subsequence solution using a custom
`Common Element Table` (CET) construction technique.
It complements the inadequacies of the Two-Pointer (TP) method
by recorrecting itself with the CET generated results.
The CET technique similarly complements its inadequacies with the TP results.
"""
import queue
import time


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
    CET : list[list, list] = [                  # Common Element Table
        [j for j in range(len(A))], [queue.Queue() for j in range(len(A))] ]
    PM : set[list[list]] = set()                # Partial/Potential Matches

    t1 = time.perf_counter()
    for j in range(len(A)):                     # Construct CET with respect due to A
        for k in range(len(B)):
            if A[j] == B[k]:                    # Find occurence of this character from A, in B
                CET[1][j].put_nowait(k)
    t2 = time.perf_counter()
    print(f"{t2- t1:.10f}")

    return CET
































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
        ( "hofubmnylkra", "pqhgxgdofcvmr"), # hofmr (5)
        ("oxcpqrsvwf", "shmtulqrypy"),      # @TODO: Currently unable to detect subsequence "qr"
        ("ABC", "DEF"),                     # ∅ (0)
    ]
    for p in pairs:
        # print(f"LCS{p} = ", TP_LCS(*p))
        cet = CET_LCS(*p)
        r1 = cet[0]
        r2 = []
        for q in cet[1]: r2.append([q.get_nowait() for e in range(q.qsize())])
        print(f"{p}\n{r1}\n{r2}\n")