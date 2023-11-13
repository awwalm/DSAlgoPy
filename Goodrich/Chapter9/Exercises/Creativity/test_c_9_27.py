import unittest
from Goodrich.Chapter9.Exercises.Creativity.C_9_27 import FifoPriorityQueue


class TestFifoPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.q = FifoPriorityQueue(1)

    def test_enqueue_dequeue(self):
        print(f"cur size: {len(self.q)}\t cur item: {self.q.dequeue()}")
        for i in range(2,11):
            self.q.enqueue(i)
            print(f"cur size: {len(self.q)}\t cur item: {self.q.dequeue()}")


if __name__ == '__main__':
    unittest.main()
