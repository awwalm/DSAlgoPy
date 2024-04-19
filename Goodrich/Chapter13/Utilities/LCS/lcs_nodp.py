"""
Non-Dynamic Programming Longest Common Subsequence solution.
Exploits the observation that if A is shorter than B, then LCS <= length of A.
But what happens when A and B are equally sized?
We compute the LCS twice, each in alternate order, and choose the longest output.

* Improves on the DP implementation by availing O(m * n) space usage.
* Reduces rate of hitting exactly m*n comparisons (per call) when partial matches are hit.
* Compromises on DP implementation by running through all inputs twice as much.

Worst case time complexity: O(2 * m * n) ~ o(mn)
Worst case space complexity: O(n) : if n >= m; else O(m)
"""
#@FIXME: Currently not a correct implementation - won't pass all test cases.


def get_lcs(A: str, B: str):
    lcs1 = get_subsequence(A, B)
    lcs2 = get_subsequence(B, A)
    return lcs1 if len(lcs1) >= len(lcs2) else lcs2

def get_subsequence(A: str, B: str):
    lcs = []
    def scan_match(J, K):
        for j in range(J, len(A)):
            for k in range(K, len(B)):
                if A[j] == B[k]:
                    lcs.append(A[j])
                    return scan_match(j+1, k+1)
    scan_match(0, 0)
    return lcs


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
        print(f"LCS{p} = ", get_lcs(*p))
