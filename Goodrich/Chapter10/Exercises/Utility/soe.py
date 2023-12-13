"""Playground implementations for Exercise C-10.31"""

def optimal_sieve(m: int):
    """Optimal Sieve of Eratosthenes algorithm that finds primes from 0 till m."""
    BA = [True] * m
    for i, k in zip(range(2, m + 1), range(2, len(BA))):
        if BA[k] is False: continue
        for j in range(i**2, m, i):
            BA[j] = False
    return [i for i,j in zip(range(2, m + 1), BA[2:]) if j is True]

def correct_sieve(m: int):
    BA = [True] * m
    rtm = int(m**(1/2)) + 1
    p = []
    for i in range(2, rtm):
        if BA[i]:           # Starts from no. 2 which is prime
            p.append(i)
            f = i
            while f < len(BA):
                BA[f] = False
                f += i
    for i in range(2, len(BA)):
        if BA[i]: p.append(i)
    return p


def SOE2(m: int):
    """Standard Sieve of Eratosthenes algorithm that finds primes from 0 till m."""
    BA = [True] * m
    for i, k in zip(range(2, (m//2) + 1), range(len(BA)//2)):
        if BA[k] is False: continue
        for j in range(2, i):
            if i % j == 0:
                BA[k] = False
                f = k + j
                while f < len(BA):
                    BA[f] = False
                    f += j
                break
    return [i for i,j in zip(range(2, m + 1), BA) if j is True]

def primes_sieve2(limit):
    """From Stackoverflow: https://stackoverflow.com/a/3941967/13488161"""
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def suboptimal_sieve(m: int):
    """Suboptimal Sieve of Eratosthenes algorithm for finding primes in range [m > 0, 2*m).\n
    :param m : Initial length specified.
    """
    BA = [True] * m
    rtm = (2*m)**(1/2)
    for i, k in zip(range(m + 1, 2 * m + 1), range(len(BA))):
        if i > 3:
            if BA[k] is False: continue
            for j in range(2, i):
                if i % j == 0:
                    BA[k] = False
                    f = k + j
                    c = 0
                    while f < len(BA) and c < rtm:
                        BA[f] = False
                        f += j
                        c += 1
                    break
    return BA

def broken_sieve(m: int):
    """Broken implementation of the Sieve of Eratosthenes algorithm for finding primes in range [m > 0, 2*m).\n
    :param m : Initial length specified.
    """
    BA = [True] * m
    rtm = (2*m)**(1/2)
    for i, k in zip(range(m + 1, 2 * m + 1), range(len(BA))):
        if i > 3:
            if BA[k] is False: continue
            for j in range(2, i):
                if i % j == 0:
                    BA[k] = False
                    f = k + j
                    while f < len(BA):
                        BA[f] = False
                        f += j
                    break
            if k + 1 > rtm: return BA

def naive_sieve(m: int):
    """Naive implementation of the Sieve of Eratosthenes algorithm for finding primes in range [m > 0, 2*m).\n
    :param m : Initial length specified.
    """
    BA = [True] * m
    for i, k in zip(range(m + 1, 2 * m + 1), range(len(BA))):
        if i > 3:
            for j in range(2, i):
                if i % j == 0:
                    BA[k] = False
                    break
    return BA
