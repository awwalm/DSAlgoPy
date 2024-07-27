"""0/1 Knapsack adapted from freecodecamp."""

from typing import List, Tuple

def knapsack(items: List[Tuple[int, int]], capacity: int):
    """
    :param capacity: Weight limit of knapsack.
    :param items: List of items represented as weight-value pairs.

    Example:

    Total capacity of container can hold 10kgs

    1 - Microwave - weight: 8, value: 50
    2 - Drone - weight: 2, value: 150
    3 - Monitor - weight: 6, value: 210
    4 - Kettle - weight: 1, value: 30

    >>> ITEMS = [(0,0), (8,50), (2,150), (6,210), (1,30)]
    >>> WEIGHTS = [] # [0, 8, 2, 6, 1]
    >>> VALUES = [] # [0, 50, 150, 210, 30]
    >>> for I in ITEMS: WEIGHTS.append(I[0])
    >>> for I in ITEMS: VALUES.append(I[1])
    >>> CAPACITY = 10
    """
    num_items = len(items)
    data = [[0 for _ in range(capacity)] for _ in range(num_items)]
    weights, values = [], []

    for w,v in items:
        weights.append(w)
        values.append(v)

    for i in range(1, num_items):
        for c in range(1, capacity):
            if weights[i] <= c:
                # Obtain maximum between...
                # (1) Inclusive Value: value at current capacity + value of preceding item
                #        (i.e. at position = current capacity - weight of current item)
                # (2) Non-inclusive Value: value at current capacity WITHOUT current item
                inclusive_value = values[i] + data[i - 1][c - weights[i]]
                noninclusive_value = data[i - 1][c]
                data[i][c] = max(inclusive_value, noninclusive_value)
            else: # weights[i] > c
                # If capacity exceeded, use value of previous item at same capacity
                data[i][c] = data[i - 1][c]

    return data


if __name__ == "__main__":
    items_ = [(0,0), (8,50), (2,150), (6,210), (1,30)]
    tab = knapsack(items_, 10)
    print()
    for row in tab:
        for r in row:
            print("%-4s " % r, end="")
        print()
