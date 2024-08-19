
# noinspection PyMethodMayBeStatic
class Solution:

    def maxSubArray1(self, nums: list[int]) -> int:
        sums = nums[0]
        for i in range(len(nums)):
            for j in range(len(nums) + 1):
                window = nums[i:j]
                if len(window) < 1: continue
                s = sum(nums[i:j])
                print(f"i = {i}\nj = {j}\ns = {s}\nsums = {sums}\n")
                if s > sums:
                    sums = s
        return sums

    def maxSubArray(self, nums: list[int]) -> int:
        max_val = nums[0]
        n = len(nums)
        if n > 1:
            for i in range(1, n):
                nums[i] = max(nums[i],
                              nums[i] + nums[i - 1])
                max_val = nums[i] if nums[i] > max_val else max_val
        return max_val



if __name__ == "__main__":
    x = [-1,-2]
    Solution().maxSubArray(x)
