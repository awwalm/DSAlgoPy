"""If a recursive call starts at most one other, we call this a linear recursion."""


def linear_sum(S, n):
    """Return the sum of the first n numbers of sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]


def reverse(S, start, stop):
    """Reverse elements in implicit slice ``S[start:stop]``."""
    if start < stop - 1:                            # If at least 2 elements.
        S[start], S[stop-1] = S[stop-1],S[start]    # Swap first and last.
        reverse(S, start+1, stop-1)                 # Recur on rest.


def power_trivial(x, n):                            # Executes in O(n) time.
    """Compute the value x**n for integer n."""
    if n == 0:
        return 1
    else:
        return x * power_trivial(x, n-1)


def power_repeat_sq(x, n):                          # Cuts n in half upon each recursive call [O(log n)].
    """Compute the value x**n for integer n."""
    if n == 0:
        return 1
    else:
        partial = power_repeat_sq(x, n//2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result
