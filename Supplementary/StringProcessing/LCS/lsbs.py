from typing import List


def LSBS(B: List[List[int]]) -> List[int]:
    """
    Longest Sorted Bucket Sequence algorithm.

    :param B The second row (buckets of indices) of CET(a,b).
    :returns: The longest sorted sequence of indices of string b, that are characters of string a.
    """
    # Flatten and sort the buckets, keeping track of original bucket indices
    # flattened = sorted((num, i) for i, bucket in enumerate(B) for num in bucket)
    flattened = []
    for i, bucket in enumerate(B):
        for num in bucket:
            flattened.append((num, i))                      # Append tuple (num, i) to the flattened list
    flattened = sorted(flattened)                           # Sort the flattened list

    n = len(flattened)
    dp = [1] * n    # Assume each element is the singleton longest increasing subsequence
    prev = [-1] * n # Previous index in the longest sequence

    longest_seq_end = 0
    for i in range(1, n):
        for j in range(i):
            if (flattened[j][1] < flattened[i][1] and       # Check if from an earlier bucket
                    flattened[j][0] < flattened[i][0] and   # Check if smaller number
                    dp[j] + 1 > dp[i]):                     # Could this iteration be one character longer?
                dp[i] = dp[j] + 1                           # Iteration `i` yields a LONGER subsequence
                prev[i] = j                                 # How did we get to `i`? It comes after `j`

        if dp[i] > dp[longest_seq_end]:                     # Determine position of longest sequence so far
            longest_seq_end = i

    # return longest_seq_end                                # If we want only length of LCS

    # Reconstruct the sequence (scanning the flattened array from behind)
    sequence = []
    if len(flattened) > 0:
        while longest_seq_end != -1:
            sequence.append(flattened[longest_seq_end][0])
            longest_seq_end = prev[longest_seq_end]

    return sequence[::-1]                                   # Reverse to get the sequence in ascending order


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [[3], [0, 4], [2], [0, 4], [1], [3], [0, 4]],
        [[1, 8, 10], [3, 6, 7], [3, 6, 7], [0], [0], [3, 6, 7], [2, 4, 5, 9, 11], [2, 4, 5, 9, 11], [3, 6, 7],
         [2, 4, 5, 9, 11]],
        [[1, 8, 10], [3, 6, 7], [3, 6, 7], [0], [0], [3, 6, 7], [2, 4, 5, 9], [2, 4, 5, 9], [3, 6, 7]],
        [[3], [0], [1], [2], [4]],
        [[], [], [], [9], [6], [7], [0], [], [], []]
    ]

    for t, case in enumerate(test_cases, 1):
        result = LSBS(case)
        print(f"Test case {t}:")
        print(f"Input: {case}")
        print(f"Output: {result}")
        print(f"Length: {len(result)}\n")
