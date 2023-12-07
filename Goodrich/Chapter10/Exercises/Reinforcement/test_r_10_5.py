import unittest
from Goodrich.Chapter10.Exercises.Reinforcement.R_10_5 import UnsortedTableMap
unittest.TestLoader.sortTestMethodsUsing = None  # Stop f#$%ing running tests in sporadic order


class TestPositionalUnsortedMap(unittest.TestCase):
    def setUp(self):
        self.s = UnsortedTableMap()

    def test1Stringified(self):
        print(f"Unsorted map created: {self.s}")
        print(self.s)

    def test2SetItem(self):
        self.s["One"] = 1
        print(self.s)
        self.assertEqual(1, self.s["One"])

    def test3BulkSetItem(self):
        self.s["One"] = 1
        self.s["Two"] = 2
        self.s["Three"] = 3
        self.s["Four"] = 4
        self.s["Five"] = 5
        self.assertEqual(len(self.s), 5)

    def test4DeleteItem(self):
        self.s["One"] = 1
        self.s["Two"] = 2
        self.s["Three"] = 3
        self.s["Four"] = 4
        self.s["Five"] = 5
        print(f"before delete: {self.s}")
        del self.s["One"]
        print(f"after delete: {self.s}")
        self.assertEqual(len(self.s), 4)

    def test5StringRep(self):
        self.s["One"] = 1
        self.s["Two"] = 2
        self.s["Three"] = 3
        self.s["Four"] = 4
        self.s["Five"] = 5
        print(self.s)

    def test6Iteration(self):
        self.s["One"] = 1
        self.s["Two"] = 2
        self.s["Three"] = 3
        self.s["Four"] = 4
        self.s["Five"] = 5
        for i in self.s: print(i.key,i.value)


if __name__ == '__main__':
    unittest.main()
