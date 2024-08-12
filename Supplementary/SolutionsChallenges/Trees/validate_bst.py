# Mock up of https://leetcode.com/problems/validate-binary-search-tree/
from collections import deque

l1 = [1,2,3,4,5]
l2 = [1,2,5,4,6,3,8]
l3 = [1,2,3,4,4,9,11]
l4 = [1,5,3,4,6]

def gen(lst):
    for item in lst: yield item


def validate2(lst):
    seq = gen(lst)
    print(lst)
    q = deque()
    for i in seq:
        q.append(i)
        if len(q) == 2:
            if q[1] <= q[0]:
                print()
                return False
            else:
                q.popleft()
    print()
    return True


def validate(lst):
    seq = gen(lst)
    print(lst)
    new = None
    q = []
    try:
        q = [next(seq), next(seq)]
        if q[1] <= q[0]:
            print()
            return False
    except StopIteration:
        print()
        return True
    while True:
        try:
            new = False
            if q[1] <= q[0]:
                print()
                return False
            print(f"q0 = {q[0]}\nq1 = {q[1]}")
            q[0] = q[1]
            q[1] = next(seq)
            new = True
        except StopIteration:
            if not new:
                print()
                return True
            elif q[1] <= q[0]:
                print()
                return False
            return True


if __name__ == "__main__":
    for L in l1,l2,l3,l4:
        print(validate(L))

