from p_6_32_array_deque import ArrayDeque

dq = ArrayDeque()
dq.add_last(5)              # [5]
print(dq)
dq.add_first(3)             # [3, 5]
print(dq)
dq.add_first(7)             # [7, 3, 5]
print(dq)
print(dq.first())           # 7 -> [7, 3, 5]
print(dq)
dq.delete_last()            # 5 -> [7, 3]
print(dq)
len(dq)                     # 2 -> [7, 3]
dq.delete_last()            # 3 -> [7]
print(dq)
dq.delete_last()            # 7 -> []
print(dq)
dq.add_first(6)             # [6]
print(dq)
print(dq.last())            # 6 -> [6]
print(dq)
print(dq.first())           # 6 -> [6]
print(dq)
dq.add_first(8)             # [8, 6]
print(dq)
print(dq.last())            # 6 -> [8, 6]
print(dq)
dq.add_first(9)             # [9, 8, 6]
print(dq)
dq.delete_first()           # 9 -> [8, 6]
print(dq)
