from typing import List


def length_of_lis(nums: List[int]):
    print(nums)
    n = len(nums)
    lis = [1] * n
    for i in range(n-1, -1, -1):
        prev_lis = [ 1 + lis[j] if nums[j] > nums[i] else lis[i] for j in range(i+1, n)]
        print(f"prev lis = {prev_lis}")
        lis[i] = max(1, max(prev_lis) if prev_lis else lis[i])
    return max(lis)


# Explanation: DP, see https://www.youtube.com/watch?v=cjWnW0hdF1Y&t=930s
def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)
    lis = [1] * n
    for i in range(n - 1, -1, -1):
        max_lis = lis[i]
        for j in range(i + 1, n):
            cur_lis = 1 + lis[j] if nums[j] > nums[i] else lis[i]
            if cur_lis > max_lis:
                max_lis = cur_lis
        lis[i] = max(1, max_lis)
    return max(lis)


def main(data):
    for d in data:
        res = length_of_lis(d)
        print(res)
        # print(res.values())
        # print(set(res.values()))
        print()


if __name__ == "__main__":
    inputs = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [7, 7, 7, 7, 7, 7, 7],
        [0, 1, 0, 3, 2, 3],
        [4, 10, 4, 3, 8, 9]
    ]
    main(inputs)
