from time import time
import sys


def lenbytes(n: int):
    """Code Fragment 5.1: An experiment to explore the relationship
     between a list’s length and its underlying size in Python.
    """
    data = []
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
        data.append(None)


def compute_average(n):
    """Code Fragment 5.4: Measuring the amortized cost of append for Python’s list class."""
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    print((end - start) / n)


if __name__ == "__main__":
    lenbytes(16)
    compute_average(16000)
