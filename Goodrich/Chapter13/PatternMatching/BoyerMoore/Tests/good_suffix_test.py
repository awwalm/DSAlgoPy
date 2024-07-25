"""Tests for the Good Suffix table heuristic for Boyer-Moore string matching."""

from Supplementary.StringProcessing.BoyerMoore.fast_good_suffix import clPreBmGs

if __name__ == "__main__":
    # Sample patterns
    patterns = ("WOWWOW",       # 25333
                "BAOBAB",       # 25555
                "ABCBAB",       # 24444
                "ANPANMAN",     # 8366666
                "10000",        # 3215
                "01010",        # 4422
                "DRIDI",        # 2555
                "TCCTATTCTT",
                )

    # Test GST construction for collection of patterns
    for pattern in patterns:
        bmGs_table = clPreBmGs(pattern)
        print(f"\nGood-Suffix Table for {pattern}:")
        print("Index\tShift Value")
        for i, shift_value in enumerate(bmGs_table):
            print(f"{i}\t\t{shift_value}")
