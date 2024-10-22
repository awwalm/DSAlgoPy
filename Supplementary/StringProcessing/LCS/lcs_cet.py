"""
Longest Common Subsequence solution using Common Element Tabale (CET) technique.
"""
from Supplementary.StringProcessing.LCS.lsbs import LSBS
from collections import deque


def CET(A: str, B: str):
    """The Common Element Table heuristic for obtaining
    all indices matching each character in string A to string B.
    """
    cet: list[list | list] = [              # Common Element Table
        [j for j in range(len(A))],         # Row 1: Indices of string A
        [deque() for _ in range(len(A))]    # Row 2: Empty queue for occurences of A[j] in B
    ]

    for j in range(len(A)):                 # Construct CET with respect due to A
        for k in range(len(B)):             # Find all occurences of A[j] in B
            if A[j] == B[k]:
                cet[1][j].append(k)         # Record matched indices in queue

    return cet


def LCS_CET(A: str, B: str):
    """Compute Longest Common Subsequence based on CET,
    using the Longest Sorted Bucket Sequence (LSBS) algorithm."""
    matching_buckets = CET(A, B)[1]         # We only need the queues (second row of CET)
    indices = LSBS(B=matching_buckets)
    matches = [B[i] for i in indices]
    return len(matches), str().join(matches)
