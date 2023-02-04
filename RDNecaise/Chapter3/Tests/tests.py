"""Script to test the MultiArray class"""

from RDNecaise.Chapter3.array import MultiArray

elements = [2, 15, 45, 13, 78, 40, 12, 52, 91, 86, 59, 25, 33, 41, 6]
m_array = MultiArray(3, 5)
m_array.clear(10)
print("Dims: ", *m_array.factors())
d1, d2 = 0, 0
for i, e in enumerate(elements):
    m_array[d1, d2] = e
    print(f"Element #{i}: {m_array[d1, d2]}")
    d2 += 1
    if d2 > 4:
        d2 = 0
        d1 += 1
    if d1 > 2:
        d1 = 0
