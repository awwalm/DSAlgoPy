"""Non-Dynamic Programming Longest Common Subsequence solution.
This piece of $#!+ took me almost 16 hours to correctly implement.

+ Improves on the DP implementation by availing O(m * n) space usage.
- Compromises on DP implementation by running through inputs twice as much.

Worst case time complexity: O(2 * m * n) -> O(mn)
Worst case time complexity: O(n) : if n >= m; else O(m)"""

def get_lcs(A, B):
    lcs1 = get_subsequence(A, B)
    lcs2 = get_subsequence(B, A)
    return lcs1 if len(lcs1) > len(lcs2) else lcs2

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
    # LCS :=    BDAB (n=4); GTTTAA (6);  GTTTA (5);   2345 (4); 123 (3);
    sequence1 = "ABCBDAB", "GTTCCTAATA", "GTTCCTAAT", "12345", "123"
    sequence2 = "BDCAB", "CGATAATTGAGA", "CGATAATTGAG", "23415", "1323"
    for x,y in zip(sequence1, sequence2):
        print("Longest Common Subsequence:", get_lcs(x, y))
