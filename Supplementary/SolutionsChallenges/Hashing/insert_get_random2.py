# https://leetcode.com/problems/insert-delete-getrandom-o1/


import random


class RandomizedSet:

    def __init__(self):
        self._size = 0
        self._index_map = dict()
        self._data = list()

    def insert(self, val: int) -> bool:
        if self._index_map.get(val) is not None:
            return False
        self._data.append(val)
        self._index_map[val] = self._size
        self._size += 1
        return True

    # The trick here is to simply fill up the deleted slot with item at the end of the list
    # And then pop that item if required. Rest, we deal with consequential edge cases.
    def remove(self, val: int) -> bool:
        ndx = self._index_map.get(val)
        if ndx is not None:
            if self._size == 1:
                self._data.pop()
            elif self._size > 1:
                self._data[ndx] = self._data[self._size - 1]
                if ndx != self._size - 1:
                    self._index_map[self._data[ndx]] = ndx
                self._data.pop()
            self._index_map.pop(val)
            self._size -= 1
            return True
        return False

    def getRandom(self) -> int:
        ndx = random.randint(0, self._size - 1)
        # print(f"random called, size = {self._size}, index = {ndx}, data = {self._data}")
        return self._data[ndx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


def test_cases(calls, data, expected=None):
    s = RandomizedSet()
    for i in range(len(calls)):
        if calls[i] == "RandomizedSet":
            print(f"s = RandomizedSet() = {None} | expected = {expected[i] if expected else None}")
        elif calls[i] == "getRandom":
            print(f"s.getRandom() = {s.getRandom()} | expected = {expected[i] if expected else '[N/A]'}")
        elif calls[i] == "remove":
            removed = data[i][0] in s._data
            print(f"s.remove({data[i][0]}) = {s.remove(data[i][0])} | expected = {expected[i] if expected else removed}")
        elif calls[i] == "insert":
            inserted = data[i][0] not in s._data
            print(f"s.insert({data[i][0]}) = {s.insert(data[i][0])} | expected = {expected[i] if expected else inserted}")
        print(f"data = {s._data}\nmap = {s._index_map}\n")


def test():
    s = RandomizedSet()
    print("s = RandomizedSet() = ", str(RandomizedSet()), " | expected = None", sep="")
    print(s._data, s._index_map, "\n")
    print("s.insert(1) = ", s.insert(1), " | expected = True", sep="")
    print(s._data, s._index_map, "\n")
    print("s.remove(2) = ", s.remove(2), " | expected = False", sep="")
    print(s._data, s._index_map, "\n")
    print("s.insert(2) = ", s.insert(2), " | expected = True", sep="")
    print(s._data, s._index_map, "\n")
    print("s.getRandom() = ", s.getRandom(), " | expected = 2", sep="")
    print(s._data, s._index_map, "\n")
    print("s.remove(1) = ", s.remove(1), " | expected = True", sep="")
    print(s._data, s._index_map, "\n")
    print("s.insert(2) = ", s.insert(2), " | expected = False", sep="")
    print(s._data, s._index_map, "\n")
    print("s.getRandom() = ", s.getRandom(), " | expected = 2", sep="")
    print(s._data, s._index_map, "\n")




if __name__ == "__main__":
    null = None
    true = True
    false = False

    cases = [
        (["RandomizedSet", "remove", "remove", "insert", "getRandom", "remove", "insert"],
        [[], [0], [0], [0], [], [0], [0]])
        ,
        (["RandomizedSet", "insert", "insert", "remove", "insert", "remove", "getRandom"],
        [[], [0], [1], [0], [2], [1], []],
        [null, true, true, true, true, true, 2])
        ,
        (["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"],
         [[],[1],[2],[2],[],[1],[2],[]],
         [null,true,false,true,1,true,false,2])
        ,
        # First test case
        (["RandomizedSet", "insert", "insert", "insert", "insert", "getRandom", "getRandom", "getRandom", "getRandom",
          "remove", "remove", "remove", "remove"],
         [[], [2], [2], [1], [1], [], [], [], [], [2], [2], [1], [1]])
        ,
        # Second test case
        (["RandomizedSet", "insert", "insert", "getRandom", "insert", "getRandom", "remove", "insert", "remove",
          "getRandom", "remove", "getRandom", "getRandom", "getRandom", "remove", "insert", "insert", "insert",
          "remove", "insert", "getRandom", "getRandom", "getRandom", "remove", "remove", "remove", "insert", "insert",
          "remove", "insert", "getRandom", "remove", "insert", "insert", "getRandom", "insert", "insert", "insert",
          "insert", "remove", "remove", "insert", "getRandom", "remove", "insert", "getRandom", "getRandom", "remove",
          "getRandom", "remove", "getRandom", "insert", "insert", "getRandom", "getRandom", "remove", "insert",
          "insert", "getRandom", "remove", "remove", "insert", "insert", "insert", "getRandom", "getRandom",
          "getRandom", "remove", "insert", "getRandom", "insert", "insert", "remove", "remove", "insert", "getRandom",
          "getRandom", "remove", "remove", "getRandom", "insert", "insert", "insert", "getRandom", "remove",
          "getRandom", "remove", "remove", "insert", "insert", "getRandom", "insert", "insert", "remove", "getRandom",
          "insert", "getRandom", "remove", "remove", "getRandom", "remove", "remove", "getRandom"],
         [[], [135], [134], [], [50], [], [50], [115], [134], [], [135], [], [], [], [115], [65], [139], [74], [65],
          [117], [], [], [], [117], [74], [139], [64], [104], [64], [97], [], [104], [54], [62], [], [119], [64], [76],
          [134], [97], [62], [57], [], [76], [134], [], [], [134], [], [119], [], [138], [147], [], [], [54], [102],
          [54], [], [57], [57], [132], [95], [109], [], [], [], [95], [100], [], [90], [139], [138], [138], [92], [],
          [], [132], [109], [], [88], [122], [102], [], [54], [], [90], [92], [89], [91], [], [60], [144], [102], [],
          [71], [], [144], [71], [], [91], [89], []])
        ,
        # Third test case
        (["RandomizedSet", "insert", "insert", "insert", "insert", "insert", "getRandom", "insert", "insert", "insert",
          "insert", "getRandom", "remove", "remove", "remove", "remove", "getRandom", "remove", "remove", "getRandom",
          "remove"],
         [[], [45], [46], [47], [48], [49], [], [51], [52], [53], [54], [], [46], [49], [48], [45], [], [47], [54], [],
          [51]])
        ,
        # Fourth test case
        (["RandomizedSet", "insert", "insert", "insert", "insert", "insert", "insert", "insert", "insert", "insert",
          "insert", "insert", "getRandom", "remove", "remove", "remove", "remove", "remove", "remove", "remove",
          "getRandom", "remove"],
         [[], [1], [2], [3], [3], [4], [5], [6], [7], [8], [9], [10], [], [1], [2], [3], [4], [5], [6], [7], [], [8]])
        ,
        # Fifth test case
        (["RandomizedSet", "insert", "insert", "insert", "insert", "insert", "insert", "insert", "insert", "insert",
          "insert", "insert", "getRandom", "remove", "remove", "remove", "remove", "remove", "remove", "remove",
          "getRandom", "remove"],
         [[], [3], [4], [5], [6], [6], [7], [8], [9], [10], [11], [12], [], [12], [11], [10], [9], [8], [7], [6], [],
          [5]])
        ,
        # Sixth test case
        (["RandomizedSet", "insert", "insert", "insert", "insert", "insert", "insert", "insert", "insert", "insert",
          "insert", "insert", "getRandom", "remove", "getRandom", "remove", "remove", "remove", "remove", "remove",
          "remove", "remove", "getRandom", "remove"],
         [[], [-3], [-2], [-1], [0], [1], [2], [2], [3], [4], [5], [6], [], [-2], [], [2], [5], [61687717], [-1], [4],
          [1], [863798724], [], [6]])
        ,
        # Seventh test case
        (["RandomizedSet", "insert", "insert", "getRandom", "remove", "insert", "getRandom", "remove", "insert",
          "getRandom", "remove", "insert", "getRandom", "remove", "insert", "getRandom", "remove", "insert",
          "getRandom", "remove", "remove", "insert"],
         [[], [1], [2], [], [1], [3], [], [2], [4], [], [3], [5], [], [4], [6], [], [5], [7], [], [6], [-1996846236],
          [8]])
        ,
        # Eighth test case
        (["RandomizedSet", "insert", "insert", "remove", "remove", "insert", "insert", "remove", "insert", "remove",
          "insert", "getRandom", "getRandom", "getRandom", "insert", "getRandom", "getRandom", "remove", "getRandom",
          "remove", "insert", "getRandom", "insert", "getRandom", "getRandom", "insert", "remove", "getRandom",
          "insert", "insert", "getRandom", "insert", "remove", "insert", "getRandom", "insert", "insert", "insert",
          "insert", "remove", "getRandom", "getRandom", "insert", "insert", "getRandom", "getRandom", "insert",
          "remove", "insert", "insert", "remove", "remove", "getRandom", "insert", "insert", "insert", "remove",
          "getRandom", "remove", "insert", "getRandom", "insert", "insert", "remove", "remove", "getRandom", "insert",
          "getRandom", "remove", "insert", "getRandom", "getRandom", "insert", "insert", "insert", "insert", "remove",
          "remove", "insert", "insert", "getRandom", "getRandom", "insert", "insert", "insert", "remove", "remove",
          "remove", "remove", "insert", "remove", "remove", "getRandom", "insert", "getRandom", "insert", "getRandom",
          "getRandom", "insert", "remove", "getRandom", "insert", "remove", "remove", "getRandom", "getRandom",
          "getRandom", "insert", "getRandom", "insert", "insert", "insert", "getRandom", "getRandom", "insert",
          "remove", "remove", "insert", "getRandom", "insert", "getRandom", "remove", "getRandom", "insert", "insert",
          "insert", "insert", "remove", "insert", "getRandom", "getRandom", "getRandom", "getRandom", "insert",
          "insert", "getRandom", "getRandom", "remove", "remove", "remove", "getRandom", "getRandom", "insert",
          "getRandom", "insert", "remove", "insert", "getRandom", "insert", "insert", "insert", "getRandom", "insert",
          "getRandom", "getRandom", "remove", "insert", "getRandom", "insert", "remove", "remove", "remove", "remove",
          "remove", "insert", "remove", "remove", "remove", "getRandom", "insert", "insert", "getRandom", "insert",
          "getRandom", "remove", "remove", "insert", "getRandom", "remove", "getRandom", "insert", "insert", "remove",
          "remove", "remove", "remove", "remove", "remove", "remove", "getRandom", "getRandom", "remove", "remove",
          "getRandom", "remove", "insert", "remove", "remove", "getRandom", "insert", "insert", "remove", "insert",
          "remove", "remove", "insert", "remove", "insert", "remove", "getRandom", "insert", "remove", "remove",
          "insert", "insert", "insert", "insert", "insert", "insert", "insert", "getRandom", "remove", "getRandom",
          "insert", "getRandom", "remove", "insert", "insert", "remove", "remove", "getRandom", "remove", "remove",
          "getRandom", "getRandom", "insert", "insert", "getRandom", "getRandom", "insert", "getRandom", "insert",
          "remove", "getRandom", "insert", "insert", "remove", "insert", "insert", "getRandom", "remove", "insert",
          "getRandom", "getRandom", "getRandom", "getRandom", "getRandom", "insert", "remove", "getRandom", "insert",
          "getRandom", "insert", "getRandom", "insert", "remove", "insert", "insert", "insert", "insert", "remove",
          "insert", "insert", "getRandom", "insert", "getRandom", "getRandom", "remove", "insert", "getRandom",
          "getRandom", "getRandom", "insert", "insert", "getRandom", "getRandom", "insert", "insert", "getRandom",
          "getRandom", "remove", "getRandom", "insert", "insert", "remove", "getRandom", "remove", "getRandom",
          "remove", "getRandom", "insert", "getRandom", "insert", "getRandom", "remove", "remove", "getRandom",
          "remove", "insert", "getRandom", "remove", "insert", "remove", "getRandom", "getRandom", "insert"],
         [[], [-20], [-47], [-20], [-47], [-119], [-119], [-119], [-99], [-99], [-121], [], [], [], [144], [], [],
          [-121], [], [144], [154], [], [-13], [], [], [16], [16], [], [-78], [44], [], [57], [154], [-25], [], [142],
          [142], [-84], [-84], [-78], [], [], [-115], [110], [], [], [26], [-13], [-122], [-14], [26], [-115], [], [-4],
          [-102], [-35], [44], [], [-84], [153], [], [-28], [-69], [-122], [-4], [], [138], [], [-102], [76], [], [],
          [133], [115], [31], [-59], [138], [-59], [147], [109], [], [], [84], [-35], [-113], [110], [147], [-25],
          [109], [66], [133], [84], [], [-71], [], [-19], [], [], [-138], [-138], [], [80], [-71], [31], [], [], [],
          [-31], [], [104], [104], [142], [], [], [55], [-35], [-69], [-92], [], [-91], [], [55], [], [-59], [104],
          [126], [14], [-91], [60], [], [], [], [], [135], [57], [], [], [60], [60], [-92], [], [], [-127], [], [-113],
          [-14], [-77], [], [79], [-20], [25], [], [100], [], [], [126], [-93], [], [128], [-59], [14], [57], [80],
          [128], [-60], [-60], [-28], [-19], [], [-131], [86], [], [-69], [], [-77], [-77], [11], [], [-31], [], [90],
          [-20], [76], [-20], [-20], [-93], [153], [25], [115], [], [], [-127], [104], [], [86], [-95], [-131], [-131],
          [], [47], [112], [90], [-105], [-69], [-69], [28], [-95], [67], [142], [], [118], [-105], [118], [149],
          [-113], [-8], [150], [150], [0], [0], [], [11], [], [35], [], [0], [76], [128], [-113], [-113], [], [66],
          [28], [], [], [111], [111], [], [], [50], [], [-76], [112], [], [46], [157], [150], [-36], [-123], [], [149],
          [134], [], [], [], [], [], [48], [128], [], [-135], [], [-133], [], [-127], [-36], [97], [97], [38], [38],
          [-127], [150], [75], [], [-75], [], [], [111], [63], [], [], [], [-107], [-107], [], [], [-42], [127], [], [],
          [-133], [], [62], [106], [135], [], [79], [], [35], [], [-32], [], [-47], [], [97], [-47], [], [-32], [-31],
          [], [75], [-118], [-107], [], [], [152]])

    ]

    for t, case in enumerate(cases): print(f"\nCASE {t+1} {'='*70}"); test_cases(*case)
    # test_cases(*cases[2])
