# @FIXME: CURRENTLY NOT A VALID SOLUTION. DO NOT USE!
# #FIXED:
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
    CET : list[list | list] = [         # Common Element Table
      [j for j in range(len(A))],       # Row 1: Indices of string A
      [deque() for _ in range(len(A))]  # Row 2: Empty queue for occurences of A[j] in B
    ]
    final_matches = []                  # Final LCS indices

    t1 = time.perf_counter()
    for j in range(len(A)):             # Construct CET with respect due to A
        for k in range(len(B)):         # Find all occurences of A[j] in B
            if A[j] == B[k]:
                CET[1][j].append(k)     # Record matched indices in queue
    t2 = time.perf_counter()
    print(f"{t2- t1:.10f}")

    cet_debug = copy.deepcopy(CET)

    potential_matches = []              # Potential LCS indices
    for j in range(len(A)):
        if len(CET[1][j]) == 0:         # Queue is empty i.e. A[j] is not in B at all
            continue
        else:
            if len(potential_matches) > 0:
                prev = potential_matches[len(potential_matches)-1]
                matched = None
                for m in CET[1][j]:     # Naive linear iteration through each queue
                    if m > prev:        # The iteration checks a sorting invariance
                        potential_matches.append(m)
                        matched = m
                        break           # We only need one element from each bucket!
                if not matched:         # Sorting invariant failed, store, reset, move to next queue
                    final_matches.append(potential_matches)
                    potential_matches = []
            else:
                m = CET[1][j].popleft()
                potential_matches.append(m)

        print(potential_matches)
    final_matches.append(potential_matches)

    # return max(final_matches, key=len)
    return cet_debug

