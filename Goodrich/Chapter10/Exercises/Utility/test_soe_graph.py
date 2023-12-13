"""Performance Comparison of Various Implementations of the Sieve of Eratosthenes."""

import time
import matplotlib.pyplot as plt
from Goodrich.Chapter10.Exercises.Creativity.C_10_31 import SOE
from Goodrich.Chapter10.Exercises.Utility.soe import optimal_sieve
from Goodrich.Chapter10.Exercises.Utility.soe import primes_sieve2
from Goodrich.Chapter10.Exercises.Utility.soe import correct_sieve

def visualize_performance():
    yt_standard = []                                # Standard implmenetation
    yt_optimal = []                                 # Optimal implementation
    yt_stackoverflow = []                           # Stackoverflow implementation
    yt_correct = []
    # xd = [x for x in range(1000, 50001, 1000)]      # 50 datapoints in intervals of 1000
    xd = [x for x in range(150, 4501, 150)]

    for dt in xd:
        for f in [
            [SOE, yt_standard],
            [optimal_sieve, yt_optimal],
            [primes_sieve2, yt_stackoverflow],
            [correct_sieve, yt_correct]
        ]:
            t1 = time.time()
            f[0](dt)
            t2 = time.time()
            f[1].append(t2-t1)

    plt.plot(xd, yt_standard, label="Standard SOE")
    plt.plot(xd, yt_optimal, label="Optimal SOE")
    plt.plot(xd, yt_stackoverflow, label="Stackoverflow SOE")
    plt.plot(xd, yt_correct, label="Correct SOE")

    plt.legend()
    plt.xlabel("Range of Primes Computed")
    plt.ylabel("Time Taken (Seconds)")
    plt.title(
        "Performance Comparison of \nVarious Implementations of the Sieve of Eratosthenes")

    plt.show()


if __name__ == '__main__':
    visualize_performance()
