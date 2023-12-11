import unittest
import time
from Goodrich.Chapter10.Exercises.Creativity.C_10_31 import (
    SOE, sieve
)


class MyTestCase(unittest.TestCase):
    def setUp(self, m = 30): #random.randrange(1,23)):
        self._m = m

    def test_soe(self):
        print(f"\nTest for range [0, {self._m}):")
        print(*SOE(self._m), sep='\n')

    def test_sieve(self):
        print(f"\nTest for range [{self._m}, {2*self._m}):")
        print(*sieve(self._m), sep='\n')

    def test_sieve_performance(self):
        print("Optimized:")
        t1 = time.time()
        for i,j in zip([n for n in range(self._m + 1, 2*self._m + 1)], sieve(self._m)):
            print(f"{i} is {'prime' if j else 'not prime'}")
        t2 = time.time()
        print(f"Speed: {t2 - t1:.8f}")


if __name__ == '__main__':
    unittest.main()
