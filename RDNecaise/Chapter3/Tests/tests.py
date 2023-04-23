"""Script to test the MultiArray class"""

from RDNecaise.Chapter3.array import MultiArray

# Example 1
elements = [2, 15, 45, 13, 78, 40, 12, 52, 91, 86, 59, 25, 33, 41, 6]
m_array = MultiArray(3, 5)
m_array.clear(10)
print("Factors: ", *m_array.factors())  # Should produce (5, 1)
d1, d2 = 0, 0
for i, e in enumerate(elements):
    m_array[d1, d2] = e
    print(f"Element #{i}: {m_array[d1, d2]}")
    d2 += 1
    if d2 > 4:  # Second dimension can't exceed 5 elements, reset back to 0 in that case.
        d2 = 0
        d1 += 1
    if d1 > 2:  # First dimension can't exceed 3 elements, reset back to 0 in that case.
        d1 = 0

# Example 2
m_array = MultiArray(3, 3, 3)
m_array.clear(10)
print("Factors: ", *m_array.factors())  # Should produce (9, 3, 1)
d1, d2, d3, i = 0, 0, 0, 0
while i < 9:
    print(f"Element #{i}: {m_array[d1, d2, d3]}")
    i += 1
    d3 += 1
    if d2 > 2 and d3 > 2:
        d1 += 1
    if d3 > 2:
        d3 = 0
        d2 += 1
    if d2 > 2:
        d2 = 0
    if d1 > 2:
        d1 = 0
