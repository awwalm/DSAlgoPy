"""Thierry LeCroq's `Fast Good Suffix computation` for Boyer-Moore string matching algorithm.

Converted from C Programming Language implementation:
- Thierry LeCroq [GitHub]: https://github.com/lecroq/goodsuff/blob/main/cl.c

Demo:
- Thierry LeCroq: https://www-igm.univ-mlv.fr/~lecroq/ta2/good-suffix.php

Theories and Notes:
- https://stackoverflow.com/questions/36426911/boyer-moore-string-matching-good-suffix-shift?rq=3
- [BESTESTEST EXPLANATION] https://www.collegesidekick.com/study-docs/4797428
- https://www.scribd.com/presentation/682371197/M4-Chapter-7
"""

def suffixes(x):
    m = len(x)
    suff = [0] * m
    mMinus1 = m - 1
    g = mMinus1
    f = g - 1
    for i in range(g - 1, -1, -1):
        if i > g and (suff[i + mMinus1 - f] != i - g):
            suff[i] = min(i - g, suff[i + mMinus1 - f])
        else:
            if i < g:
                g = i
            f = i
            while g >= 0 and (x[g] == x[g + mMinus1 - f]):
                g -= 1
            suff[i] = f - g
    return suff

def clPreBmGs(x):
    """Classic preprocessing of Boyer-Moore Good Suffix Table."""
    m = len(x)
    bmGs = [0] * m
    suff = suffixes(x)
    j = 0
    mMinus1 = m - 1
    mMinus2 = mMinus1 - 1
    for i in range(mMinus2, -1, -1):
        if suff[i] == i + 1:
            for j in range(j, mMinus1 - i):
                bmGs[j] = mMinus1 - i
    for j in range(j, m):
        bmGs[j] = m
    for i in range(mMinus2 + 1):
        bmGs[mMinus1 - suff[i]] = mMinus1 - i
    return bmGs


if __name__ == "__main__":
    # Sample patterns
    patterns = ("WOWWOW",       # 25333
                "BAOBAB",       # 25555
                "ABCBAB",       # 24444
                "ANPANMAN",     # 8366666
                "10000",        # 3215
                "01010",        # 4422
                "DRIDI",        # 2555
                "TCCTATTCTT",
                )

    # Test GST construction for collection of patterns
    for pattern in patterns:
        bmGs_table = clPreBmGs(pattern)
        print(f"\nGood-Suffix Table for {pattern}:")
        print("Index\tShift Value")
        for svi, shift_value in enumerate(bmGs_table):
            print(f"{svi}\t\t{shift_value}")
