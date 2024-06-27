# https://leetcode.com/problems/climbing-stairs/description/
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

# Naive recursive
def CS_NR(s: int, n: int, opt: list[int]):
    """
    s   - Initial step, ideally starts at 0.
    n   - Number of stairs to climb.
    opt - Choices of steps to take at once.
    """
    if s < n:           # s < n [Climb higher with all options]
        opt1 = CS_NR(s + opt[0], n, opt)
        opt2 = CS_NR(s + opt[1], n, opt)
        return opt1 + opt2
    elif n - s == 0:    # s = n [We've found 1 way for now]
        return 1
    else:               # s > n [Invalid step, zero ways]
        return 0


# Memoized recursive
def CS_MR(s: int, n: int, opt: list, memo: dict):
    subsolution = memo.get((s, n))
    if subsolution:
        return subsolution
    elif s < n:
        opt1 = CS_MR(s + opt[0], n, opt, memo)
        opt2 = CS_MR(s + opt[1], n, opt, memo)
        memo[(s, n)] = opt1 + opt2
    elif n - s == 0:
        memo[(s, n)] = 1
    else:
        memo[(s, n)] = 0
    return memo[(s, n)]


# Constant space DP [Fibonacci style only valid for opt={1,2}]
def CS_DP(n: int):
    fib2, fib3, fibn = 1, 2, -1
    if 0 < n < 2:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(3, n+1):
            fibn = fib2 + fib3
            fib2 = fib3
            fib3 = fibn
        return fibn


if __name__ == "__main__":
    stairs = 2,3,4,5  # 2, 3, 5, 8
    for destination in stairs:
        nr = CS_NR(0, destination, [1,2])
        mr = CS_MR(0, destination, [1,2], dict())
        dp = CS_DP(destination)
        print(f"Naive CS({destination}) = {nr}")
        print(f"Memoized CS({destination}) = {mr}")
        print(f"Constant space DP CS({destination}) = {dp}")


