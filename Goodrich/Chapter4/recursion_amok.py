"""Although recursion is a very powerful tool, it can easily be misused in various ways. 
In this section, we examine several problems in which
a poorly implemented recursion causes drastic inefficiency.
"""


def unique3(S, start, stop):
    """Return ``True`` if there are no duplicate elements in slice ``S[start:Stop].``"""
    if stop - start <= 1:
        return True  # At most one item.
    elif not unique3(S, start, stop - 1):
        return False  # First part has duplicate.


def bad_fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)


def good_fibonacci(n):
    """Return pair of Fibonacci numbers, ``F(n), F(n-1)``."""
    if n <= 1:
        return n, 0
    else:
        a, b = good_fibonacci(n-1)
        return a + b, a
