"""C-10.31 For an ideal compression function, the capacity of the bucket array for a hash table
should be a prime number. Therefore, we consider the problem of locating a prime number in a range [M,2M].
Implement a method for finding such a prime by using the sieve algorithm.
In this algorithm, we allocate a 2M cell Boolean array A, such that cell i is associated with the integer i.
We then initialize the array cells to all be “true” and we “mark off” all the cells
that are multiples of 2, 3, 5, 7, and so on. This process can stop after it reaches a number larger than
√ 2M. (Hint: Consider a bootstrapping method for finding the primes up to √ 2M)"""
# @TODO: Works but needs improvement - find a way to generate primes until  √ 2M

def soe(m: int):
    """Efficient and fast Sieve of Eratosthenes algorithm that finds primes from 0 till m."""
    BA = [True] * m
    rtm = int(m**(1/2)) + 1
    for i in range(2, len(BA)):
        if BA[i]:
            yield i
            if i < rtm:
                f = i
                while f < len(BA):
                    BA[f] = False
                    f += i

def sieve(m: int):
    """Lazy Sieve of Eratosthenes algorithm for finding primes in range [m > 0, 2*m).\n
    :param m : Initial length specified.
    """
    BA = [True] * m
    rtm = (2*m)**(1/2)
    lim = []
    for x in soe(m):
        lim.append(x)
        if x > rtm:
            break
    for i, k in zip(range(m + 1, 2 * m + 1), range(len(BA))):
        if BA[k] is False: continue
        for j in lim:
            if i % j == 0:
                BA[k] = False
                break
    return [i for i, j in zip(range(m + 1, 2 * m + 1), BA) if j is True]
