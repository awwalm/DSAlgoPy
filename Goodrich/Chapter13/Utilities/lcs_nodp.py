"""Non-Dynamic Programming Longest Common Subsequence solution.
This piece of $#!+ took me almost 16 hours to correctly implement.

+ Exploits the observation that if A is shorter than B, then LCS <= length of A.
+ Improves on the DP implementation by availing O(m * n) space usage.
+ Reduces rate of hitting exactly m*n comparisons when partial matches are hit.

Worst case time complexity: O(mn)
Worst case space complexity: O(n) : if n >= m; else O(m)"""


def get_lcs(A, B):
    shorter = A if len(A) < len(B) else B
    longer = B if shorter == A else A
    return get_subsequence(shorter, longer)

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
    # LCS :=    BDAB (n=4); GTTTAA (6);  GTTTA (5);   2345 (4); 123 (3); 2654 (4)
    sequence1 = "ABCBDAB", "GTTCCTAATA", "GTTCCTAAT", "12345", "123", "126548"
    sequence2 = "BDCAB", "CGATAATTGAGA", "CGATAATTGAG", "23415", "1323", "216544"
    for x,y in zip(sequence1, sequence2):
        print("Longest Common Subsequence:", get_lcs(x, y))
