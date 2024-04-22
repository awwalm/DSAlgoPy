
from collections import deque

# Longest Sorted Bucket Sequence
def LSBS(B):
    B = [deque(i) for i in B]
    PM = []
    pm = []
    for j in range(len(B)):
        if len(B[j]) == 0:
            continue
        else:
            if len(pm) > 0:
                prev = pm[len(pm)-1]
                matched = None
                for m in B[j]:
                    if m > prev:
                        pm.append(m)
                        matched = m
                        break
                if not matched:
                    PM.append(pm)
                    pm = []
            else:
                m = B[j].popleft()
                pm.append(m)

    PM.append(pm)
    return max(PM, key=len)


def LIS(X):
    """Returns the Longest Increasing Subsequence in the Given List/Array"""
    N = len(X)
    P = [0] * N
    M = [0] * (N + 1)
    L = 0
    for i in range(N):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo + hi) // 2
            if X[M[mid]] < X[i]:
                lo = mid + 1
            else:
                hi = mid - 1

        newL = lo
        P[i] = M[newL - 1]
        M[newL] = i

        if newL > L:
            L = newL

    S = []
    k = M[L]
    for i in range(L - 1, -1, -1):
        S.append(X[k])
        k = P[k]
    return S[::-1]




if __name__ == "__main__":
    # Output = [0, 1, 3, 4]; [0, 2, 3, 4] is also correct
    B1 = [
        [3], [0, 4], [2], [0, 4], [1], [3], [0, 4]
    ]

    # Output = [0, 3, 4, 5, 6, 9]; [1, 3, 6, 7, 9, 11] is also correct
    B2 = [
        [1, 8, 10], [3, 6, 7], [3, 6, 7], [0], [0], [3, 6, 7],
        [2, 4, 5, 9, 11], [2, 4, 5, 9, 11], [3, 6, 7], [2, 4, 5, 9, 11]
    ]

    # Output = [0, 3, 4, 5, 6]; [0, 3, 4, 5, 7] and [1, 3, 6, 7, 9] are also correct
    B3 = [
        [1, 8, 10], [3, 6, 7], [3, 6, 7], [0], [0],
        [3, 6, 7], [2, 4, 5, 9], [2, 4, 5, 9], [3, 6, 7]
    ]

    # Output = [0, 1, 2, 4]; code produces [1, 2, 4] instead
    B4 = [
        [3], [0], [1], [2], [4]
    ]

    # Output = [6, 7]; code produces [6] instead
    B5 = [
        [], [], [], [9], [6], [7], [0], [], [], []
    ]


    # Driver code
    for c,b in enumerate([B1,B2,B3,B4,B5]):

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

        srep = []
        astr = pairs[c][0]          # A string
        bstr = pairs[c][1]          # B string
        calclsbs = LSBS(b)
        print(f"A = {astr}\nB = {bstr}")
        print(f"{b}\n{calclsbs}")   # b = CET bucket array (common indices of elements of A in B)
        for buck in b:
            for num in buck:
                if num is not None: srep.append(num)
        #print(f"CET concatenated: {srep}\n")
        print(f"LIS(b) = {LIS(srep)}\n")

