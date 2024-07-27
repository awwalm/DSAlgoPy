"""
Adapted from: https://www.youtube.com/watch?v=gCRw7BIrLPY
"""
import itertools

CAPACITY = 50
ITEMS = [
    {"weight": 10, "value": 60},
    {"weight": 20, "value": 100},
    {"weight": 30, "value": 120},
    {"weight": 25, "value": 80},
    {"weight": 15, "value": 40},
    {"weight": 5, "value": 30},
    {"weight": 22, "value": 50},
    {"weight": 18, "value": 70},
    {"weight": 11, "value": 45},
    {"weight": 9, "value": 55},
    {"weight": 14, "value": 65},
    {"weight": 12, "value": 60},
    {"weight": 7, "value": 20},
    {"weight": 8, "value": 25},
    {"weight": 13, "value": 55},
]


def knapsack_brute_force(items: list[dict[str, int]], capacity: int):
    n = len(items)
    best_value = 0
    best_combination = None
    used_capacity = None

    for r in range(n + 1):
        for combination in itertools.combinations(items, r):
            total_weight = sum(item["weight"] for item in combination)
            total_value = sum(item["value"] for item in combination)
            if total_weight <= capacity and total_value > best_value:
                best_value = total_value
                best_combination = combination
                used_capacity = total_weight

    return best_value, used_capacity, best_combination


def knapsack_greedy(items: list[dict[str, int]], capacity: int):
    items_sorted = sorted(items, key=lambda x: x["value"] / x["weight"], reverse=True)
    total_value = 0
    total_weight = 0
    chosen_items = []

    for item in items_sorted:
        if total_weight + item["weight"] <= capacity:
            chosen_items.append(item)
            total_weight += item["weight"]
            total_value += item["value"]

    return total_value, chosen_items, total_weight


# dp[i][w] = -> Best possible value for weight limit w by using first i items
def knapsack_dynamic(items: list[dict[str, int]], capacity: int):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif items[i-1]["weight"] <= w:
                dp[i][w] = max(
                    items[i-1]["value"] + dp[i-1][w-items[i-1]["weight"]],
                    dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    w = capacity
    chosen_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen_items.append(items[i-1])
            w -= items[i-1]["weight"]

    total_value = dp[n][capacity]
    return total_value, chosen_items



if __name__ == "__main__":
    ksb = knapsack_brute_force(items=ITEMS, capacity=CAPACITY)
    ksg = knapsack_greedy(items=ITEMS, capacity=CAPACITY)
    ksdp = knapsack_dynamic(items=ITEMS, capacity=CAPACITY)
    print(f"Brute Force: {ksb}")
    print(f"Greedy: {ksg}")
    print(f"Dynamic Programming: {ksdp}")
