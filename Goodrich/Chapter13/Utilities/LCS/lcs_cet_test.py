"""
Longest Common Subsequence solution using a custom
`Common Element Table` (CET) construction technique.
It complements the inadequacies of the Two-Pointer (TP) method
by recorrecting itself with the CET generated results.
The CET technique similarly complements its inadequacies with the TP results.
"""
from collections import deque
import time
import copy



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
    CET : list[list, list] = [              # Common Element Table
        [j for j in range(len(A))], [deque() for j in range(len(A))] ]
    PM = []            # Partial/Potential LCS indices

    t1 = time.perf_counter()
    for j in range(len(A)):                 # Construct CET with respect due to A
        for k in range(len(B)):             # Find all occurences of A[j] in B
            if A[j] == B[k]:
                CET[1][j].append(k)     # Record matched indices in queue
    t2 = time.perf_counter()
    print(f"{t2- t1:.10f}")

    cet_debug = copy.deepcopy(CET)

    pm = []
    for j in range(len(A)):
        k = j
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
                    PM.append(pm)
                    pm = []
            else:
                m = CET[1][j].popleft()
                pm.append(m)
                matched = m

        print(pm)
    PM.append(pm)


    return cet_debug
































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
        ("oxcpqrsvwf", "shmtulqrypy"),      # qr (2) @TODO: Bug-fixing in progress
        ("ABC", "DEF"),                     # ∅ (0)
    ]
    for p in pairs:
        # print(f"LCS{p} = ", TP_LCS(*p))
        cet = CET_LCS(*p)
        r1 = cet[0]
        r2 = []
        for q in cet[1]: r2.append([q.popleft() for e in range(len(q))])
        print(f"{p}\n{r1}\n{r2}\n")
