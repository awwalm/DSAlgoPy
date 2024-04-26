import unittest
from Goodrich.Chapter13.Utilities.LCS.lcs_tp import *

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.pairs = [
            ("ABCBDAB", "BDCAB"),  # BDAB (n=4)
            ("GTTCCTAATA", "CGATAATTGAGA"),  # GTTTAA (6)
            ("GTTCCTAAT", "CGATAATTGAG"),  # GTTTA (5)
            ("12345", "23415"),  # 2345 (4)
            ("123", "1323"),  # 123 (3)
            ("126548", "216544"),  # 2654 or 1654 (4)
            ("AGGTAB", "GXTXAYB"),  # GTAB (4)
            ("BD", "ABCD"),  # BD (2)
            ("ABCDGH", "AEDFHR"),  # ADH (3)
            ("ABCDE", "ACE"),  # ACE (3)
            ("hofubmnylkra", "pqhgxgdofcvmr"),  # hofmr (5)
            ("oxcpqrsvwf", "shmtulqrypy"),  # @TODO: Currently unable to detect subsequence "qr"
            ("ABC", "DEF"),  # ∅ (0)
        ]

    def test_correctness(self):
        self.assertEqual("".join(get_lcs(*self.pairs[0])), "BDAB")
        self.assertEqual("".join(get_lcs(*self.pairs[1])), "GTTTAA")
        self.assertEqual("".join(get_lcs(*self.pairs[2])), "GTTTA")
        self.assertEqual("".join(get_lcs(*self.pairs[3])), "2345")
        self.assertEqual("".join(get_lcs(*self.pairs[4])), "123")
        self.assertEqual("".join(get_lcs(*self.pairs[5])), "1654")
        self.assertEqual("".join(get_lcs(*self.pairs[6])), "GTAB")
        self.assertEqual("".join(get_lcs(*self.pairs[7])), "BD")
        self.assertEqual("".join(get_lcs(*self.pairs[8])), "ADH")
        self.assertEqual("".join(get_lcs(*self.pairs[9])), "ACE")
        self.assertEqual("".join(get_lcs(*self.pairs[10])), "hofmr")
        self.assertEqual("".join(get_lcs(*self.pairs[11])), "qr")  # This test will fail, bug is yet to be fixed
        self.assertEqual("".join(get_lcs(*self.pairs[12])), "")

        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
