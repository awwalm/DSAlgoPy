"""Code Fragment 13.6: Dynamic Programming algorithm for the LCS problem."""

def LCS(X, Y):
    """Return table such that L[j][k] is length of LCS for X[0:j] and Y[0:k]."""
    n, m = len(X), len(Y)                   # Introduce convenient notations
    L = [[0] * (m+1) for _ in range(n+1)]   # (n+1) * (m+1) table
    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]:                # Align this match
                L[j+1][k+1] = L[j][k] + 1
            else:                           # Choose to ignore once character
                L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
    return L


def LCS_solution(X, Y, L):
    """Return the longest common substring of X and Y, given LCS table L."""
    solution = []
    j,k = len(X), len(Y)
    while L[j][k] > 0:
        if X[j-1] == Y[j-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif L[j-1][k] >= L[j][k-1]:
            j -= 1
        else:
            k -= 1
    return "".join(reversed(solution))

