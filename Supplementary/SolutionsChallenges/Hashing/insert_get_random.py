# https://leetcode.com/problems/insert-delete-getrandom-o1/


import random


class RandomizedSet:

    def __init__(self):
        self._capacity =20
        self._data: list[int|None] = [None] * self._capacity
        self._probed = dict()
        self._set = set()
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, item):
        if item == self._get(item)[2]:
            return True
        return False

    def _hash(self, item):
        return hash(id(item)) % self._capacity

    def _probe(self, ndx):
        """Linear probing: Guranteed to return empty slot."""
        if ndx >= self._capacity:
            ndx = self._capacity - 1
        while self._data[ndx]:
            ndx = (ndx + 1) # % (self._capacity - 1)
            if ndx >= self._capacity: ndx = 0
        return ndx

    def _resize(self):
        old = self._data
        self._capacity *= 2
        self._data = [None] * self._capacity
        for i in old:
            if i:
                ndx = self._hash(i)
                if not self._data[ndx]:
                    self._data[ndx] = i
                else:
                    ndx = self._probe(ndx)
                    self._data[ndx] = i
                    self._probed[i] = ndx

    def _get(self, item):
        """
        Returns a triplet (item, index, boolean) describing the search results.
        index is -1, and boolean is false if item is not found.
        """
        ndx = self._hash(item)
        query = self._data[ndx]
        if query:
            if query == item:
                return item, ndx, True
        ndx = self._probed.get(item)
        if ndx:
            return item, ndx, True
        else:
            return item, -1, False

    def insert(self, val: int) -> bool:
        if val in self._set:
            return False
        if self._size == self._capacity:
            self._resize()
        ndx = self._hash(val)
        if self._data[ndx]:
            ndx = self._probe(val)
            self._probed[val] = ndx
        self._data[ndx] = val
        self._set.add(val)
        self._size += 1
        return True

    def remove(self, val: int) -> bool:
        if self._size > 0:
            search = self._get(val)
            if val not in self._set:
                return False
            self._data[search[1]] = None
            if self._probed.get(search[0]):
                self._probed.pop(search[0])
            self._set.remove(val)
            self._size -= 1
            return True
        return False

    def getRandom(self) -> int:
        try:
            popped = self._set.pop()
            self._set.add(popped)
            return popped
        except Exception:
            ndx = random.randint(0,self._capacity-1)
            anonymous = self._data[ndx]
            if anonymous: return anonymous
            popped = self._set.pop()
            self._set.add(popped)
            return popped


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
        print(f"data = {s._data}\nmap = {list(s._set)}\n")


def test():
    s = RandomizedSet()
    print(s)

    print("s.insert(1) = ", s.insert(1), sep="")
    print("s.remove(2) = ", s.remove(2), sep="")
    print("s.insert(2) = ", s.insert(2), sep="")
    print("s.getRandom() = ", s.getRandom(), sep="")
    print("s.remove(1) = ", s.remove(1), sep="")
    print("s.insert(2) = ", s.insert(2), sep="")
    print("s.getRandom() = ", s.getRandom(), sep="")




if __name__ == "__main__":
    # test()

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
        (["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
         [[], [1], [2], [2], [], [1], [2], []],
         [null, true, false, true, 1, true, false, 2])
        ,
        # First test case
        (["RandomizedSet", "insert", "insert", "insert", "insert", "getRandom", "getRandom", "getRandom", "getRandom",
          "remove", "remove", "remove", "remove"],
         [[], [2], [2], [1], [1], [], [], [], [], [2], [2], [1], [1]])
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
        (["RandomizedSet","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove","remove"],
         [[],[1000000000],[1000000001],[1000000002],[1000000003],[1000000004],[1000000005],[1000000006],[1000000007],[1000000008],[1000000009],[1000000010],[1000000011],[1000000012],[1000000013],[1000000014],[1000000015],[1000000016],[1000000017],[1000000018],[1000000019],[1000000020],[1000000021],[1000000022],[1000000023],[1000000024],[1000000025],[1000000026],[1000000027],[1000000028],[1000000029],[1000000030],[1000000031],[1000000032],[1000000033],[1000000034],[1000000035],[1000000036],[1000000037],[1000000038],[1000000039],[1000000040],[1000000041],[1000000042],[1000000043],[1000000044],[1000000045],[1000000046],[1000000047],[1000000048],[1000000049],[1000000050],[1000000051],[1000000052],[1000000053],[1000000054],[1000000055],[1000000056],[1000000057],[1000000058],[1000000059],[1000000060],[1000000061],[1000000062],[1000000063],[1000000064],[1000000065],[1000000066],[1000000067],[1000000068],[1000000069],[1000000070],[1000000071],[1000000072],[1000000073],[1000000074],[1000000075],[1000000076],[1000000077],[1000000078],[1000000079],[1000000080],[1000000081],[1000000082],[1000000083],[1000000084],[1000000085],[1000000086],[1000000087],[1000000088],[1000000089],[1000000090],[1000000091],[1000000092],[1000000093],[1000000094],[1000000095],[1000000096],[1000000097],[1000000098],[1000000099],[-1000000000],[-1000000001],[-1000000002],[-1000000003],[-1000000004],[-1000000005],[-1000000006],[-1000000007],[-1000000008],[-1000000009],[-1000000010],[-1000000011],[-1000000012],[-1000000013],[-1000000014],[-1000000015],[-1000000016],[-1000000017],[-1000000018],[-1000000019],[-1000000020],[-1000000021],[-1000000022],[-1000000023],[-1000000024],[-1000000025],[-1000000026],[-1000000027],[-1000000028],[-1000000029],[-1000000030],[-1000000031],[-1000000032],[-1000000033],[-1000000034],[-1000000035],[-1000000036],[-1000000037],[-1000000038],[-1000000039],[-1000000040],[-1000000041],[-1000000042],[-1000000043],[-1000000044],[-1000000045],[-1000000046],[-1000000047],[-1000000048],[-1000000049],[-1000000050],[-1000000051],[-1000000052],[-1000000053],[-1000000054],[-1000000055],[-1000000056],[-1000000057],[-1000000058],[-1000000059],[-1000000060],[-1000000061],[-1000000062],[-1000000063],[-1000000064],[-1000000065],[-1000000066],[-1000000067],[-1000000068],[-1000000069],[-1000000070],[-1000000071],[-1000000072],[-1000000073],[-1000000074],[-1000000075],[-1000000076],[-1000000077],[-1000000078],[-1000000079],[-1000000080],[-1000000081],[-1000000082],[-1000000083],[-1000000084],[-1000000085],[-1000000086],[-1000000087],[-1000000088],[-1000000089],[-1000000090],[-1000000091],[-1000000092],[-1000000093],[-1000000094],[-1000000095],[-1000000096],[-1000000097],[-1000000098],[-1000000099],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[1000000000],[1000000001],[1000000002],[1000000003],[1000000004],[1000000005],[1000000006],[1000000007],[1000000008],[1000000009],[1000000010],[1000000011],[1000000012],[1000000013],[1000000014],[1000000015],[1000000016],[1000000017],[1000000018],[1000000019],[1000000020],[1000000021],[1000000022],[1000000023],[1000000024],[1000000025],[1000000026],[1000000027],[1000000028],[1000000029],[1000000030],[1000000031],[1000000032],[1000000033],[1000000034],[1000000035],[1000000036],[1000000037],[1000000038],[1000000039],[1000000040],[1000000041],[1000000042],[1000000043],[1000000044],[1000000045],[1000000046],[1000000047],[1000000048],[1000000049],[1000000050],[1000000051],[1000000052],[1000000053],[1000000054],[1000000055],[1000000056],[1000000057],[1000000058],[1000000059],[1000000060],[1000000061],[1000000062],[1000000063],[1000000064],[1000000065],[1000000066],[1000000067],[1000000068],[1000000069],[1000000070],[1000000071],[1000000072],[1000000073],[1000000074],[1000000075],[1000000076],[1000000077],[1000000078],[1000000079],[1000000080],[1000000081],[1000000082],[1000000083],[1000000084],[1000000085],[1000000086],[1000000087],[1000000088],[1000000089],[1000000090],[1000000091],[1000000092],[1000000093],[1000000094],[1000000095],[1000000096],[1000000097],[1000000098],[1000000099],[-1000000000],[-1000000001],[-1000000002],[-1000000003],[-1000000004],[-1000000005],[-1000000006],[-1000000007],[-1000000008],[-1000000009],[-1000000010],[-1000000011],[-1000000012],[-1000000013],[-1000000014],[-1000000015],[-1000000016],[-1000000017],[-1000000018],[-1000000019],[-1000000020],[-1000000021],[-1000000022],[-1000000023],[-1000000024],[-1000000025],[-1000000026],[-1000000027],[-1000000028],[-1000000029],[-1000000030],[-1000000031],[-1000000032],[-1000000033],[-1000000034],[-1000000035],[-1000000036],[-1000000037],[-1000000038],[-1000000039],[-1000000040],[-1000000041],[-1000000042],[-1000000043],[-1000000044],[-1000000045],[-1000000046],[-1000000047],[-1000000048],[-1000000049],[-1000000050],[-1000000051],[-1000000052],[-1000000053],[-1000000054],[-1000000055],[-1000000056],[-1000000057],[-1000000058],[-1000000059],[-1000000060],[-1000000061],[-1000000062],[-1000000063],[-1000000064],[-1000000065],[-1000000066],[-1000000067],[-1000000068],[-1000000069],[-1000000070],[-1000000071],[-1000000072],[-1000000073],[-1000000074],[-1000000075],[-1000000076],[-1000000077],[-1000000078],[-1000000079],[-1000000080],[-1000000081],[-1000000082],[-1000000083],[-1000000084],[-1000000085],[-1000000086],[-1000000087],[-1000000088],[-1000000089],[-1000000090],[-1000000091],[-1000000092],[-1000000093],[-1000000094],[-1000000095],[-1000000096],[-1000000097],[-1000000098],[-1000000099]])

    ]

    for t, case in enumerate(cases): print(f"\nCASE {t + 1} {'=' * 70}"); test_cases(*case)
