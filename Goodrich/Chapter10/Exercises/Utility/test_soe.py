import time
import unittest
from Goodrich.Chapter10.Exercises.Utility.soe import *


class MyTestCase(unittest.TestCase):
    def setUp(self, m = int(100)): #random.randrange(1,23)):
        self._m = m
        print(f"\nInitializing m = {self._m}:")

    def test_correct_lowspace_sieve(self):
        print(f"\nLowspace Correct Sieve Test for range [0, {self._m}):")
        t1 = time.time()
        print(*lowspace_sieve(self._m), sep='\n')
        t2 = time.time()
        print(f"Lowspace Correct Sieve Speed: {t2 - t1:.8f}")

    def test_correct_sieve(self):
        print(f"\nCorrect Sieve Test for range [0, {self._m}):")
        t1 = time.time()
        print(*correct_sieve(self._m), sep='\n')
        t2 = time.time()
        print(f"Correct Sieve Speed: {t2 - t1:8f}")

    def test_optimal_sieve(self):
        print(f"\nOptimal Sieve Test for range [0, {self._m}):")
        t1 = time.time()
        print(*optimal_sieve(self._m), sep='\n')
        t2 = time.time()
        print(f"Optimal Sieve Speed: {t2 - t1:8f}")

    def test_standard_sieve(self):
        print(f"\nStandard Sieve Test for range [0, {self._m}):")
        t1 = time.time()
        print(*SOE(self._m), sep='\n')
        t2 = time.time()
        print(f"Standard Sieve Speed: {t2 - t1:8f}")

    def test_stackoverflow_sieve(self):
        print(f"\nStackoverflow Sieve Test for range [0, {self._m}):")
        t1 = time.time()
        print(*primes_sieve2(self._m), sep='\n')
        t2 = time.time()
        print(f"Stackoverflow Sieve Speed: {t2 - t1:8f}")

    def compare_standard_and_optimal(self):
        self.test_correct_lowspace_sieve()
        self.test_correct_sieve()
        self.test_optimal_sieve()
        self.test_standard_sieve()
        self.test_stackoverflow_sieve()

    """def test_naive_sieve_performance(self):
        print("Naive:")
        t1 = time.time()
        for i,j in zip([n for n in range(self._m + 1, 2*self._m + 1)], naive_sieve(self._m)):
            print(f"{i} is {'prime' if j else 'not prime'}")
        t2 = time.time()
        print(f"Speed: {t2 - t1:8f}")

    def test_compare_naivesieve_and_sieve(self):
        unop = naive_sieve(self._m)
        op = suboptimal_sieve(self._m)
        comparisons = [x is y for x,y in zip(unop, op)]
        ranges = [n for n in range(self._m + 1, 2*self._m + 1)]
        results = {i : j for i,j in zip(ranges, comparisons)}
        for r in results.keys():
            if results[r] is False:
                print(f"{r} wrongly evaluated as prime")"""


if __name__ == '__main__':
    unittest.main()
