import time
import math
import numpy as np
import matplotlib.pyplot as plt

def naive_sieve(m: int):
    BA = [True] * m
    for i, k in zip(range(2, m + 1), range(len(BA))):
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

def suboptimal_sieve(m: int):
    BA = [True] * m
    for i, k in zip(range(2, m + 1), range(2, len(BA))):
        if BA[k] is False: continue
        for j in range(i**2, m, i):
            BA[j] = False
    return [i for i,j in zip(range(2, m + 1), BA[2:]) if j is True]

def fast_sieve(m: int):
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

def pidelport_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

def numpy_sieve(bound):
    sieve = np.ones(bound, dtype=bool)  # default all prime
    sieve[:2] = False  # 0, 1 is not prime
    sqrt_bound = math.ceil(math.sqrt(bound))
    for i in range(2, sqrt_bound):
        if sieve[i]:
            inc = i if i == 2 else 2 * i
            sieve[i * i:bound:inc] = False
    return np.arange(bound)[sieve]

def visualize_performance():
    yt_naive = []
    yt_suboptimal = []
    yt_fast = []
    yt_pidelport = []
    yt_numpy = []
    # xd = [x for x in range(100, 5001, 100)]
    xd = [x for x in range(int(250e6), int(1e9)+1, int(250e6))]

    for dt in xd:
        for f in [
            # [naive_sieve, yt_naive],
            # [suboptimal_sieve, yt_suboptimal],
            [fast_sieve, yt_fast],
            [pidelport_sieve, yt_pidelport],
            [numpy_sieve, yt_numpy]
        ]:
            t1 = time.time()
            f[0](dt)
            t2 = time.time()
            f[1].append(t2-t1)

    fig = plt.figure()
    gs = fig.add_gridspec(1, 2)
    line, box = gs.subplots(sharey=False)

    # Line graph
    # line.plot(xd, yt_naive, label="Naive SOE")
    # line.plot(xd, yt_suboptimal, label="Suboptimal SOE")
    line.plot(xd, yt_fast, label="Fast SOE")
    line.plot(xd, yt_pidelport, label="Pi Delport's SOE")
    line.plot(xd, yt_numpy, label="NumPy SOE")
    line.set(xlabel="\nRange of Primes Computed", ylabel="Time Taken (Seconds)\n")
    line.set_title("Benchmark per Range")
    line.legend()

    # Box plot
    # box.boxplot([yt_naive, yt_suboptimal, yt_fast, yt_pidelport, yt_numpy])
    box.boxplot([yt_fast, yt_pidelport, yt_numpy])
    # box.set(xlabel="\nSOE Algorithms", xticklabels=["Naive", "Suboptimal", "Fast", "Pi Delport's", "NumPy"])
    box.set(xlabel="\nSOE Algorithms", xticklabels=["Fast", "Pi Delport's", "NumPy"])
    box.set_title("Average Benchmark Duration")

    plt.suptitle("Performance Comparison of \nVarious Implementations of the Sieve of Eratosthenes")
    plt.show()

if __name__ == '__main__':
    visualize_performance()