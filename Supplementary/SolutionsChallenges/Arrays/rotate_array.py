"""
https://leetcode.com/problems/rotate-array/

# Striclty In-Place Algorithm ($O(Kn)$ Time)

* First we consider the in-place solution which uses O(K * n) time and constant space in the worst case.
* However, this incites TLE once K exceeds a certain treshold (at the moment of writing; `k >= 5000`).
* As usual, we filter K for circularity to make sure we perform no operations than is necessary (`k = k % len(nums)`).
* Unfortunately, this threhold must be hardcoded, then the traditional O(K) space and O(n) time algorithm is favored.
* The in-place algorithm operates around the idea _shifting-forward-by-one_ principle, which temporarily stores that last item elswhere.
* Then, shifts everything else from the start (excluding the previous last item) forwards by one step.
* The first item in modified list (now duplicated due to the shifting) is then replaced by the temp item.
* This procedure is performed a total of K times.


<hr>

# Alternate $O(K)$ Space/$O(n)$ Time Approach

There are THREE main ideas (first two are critical; the algorithm is still correct without taking the third into consideration but is suboptimal):

- Determine the number of single rotations $k_i$ to be made (totaling to $K$).

- If number of rotations ($K$) is equivalent to the number of elements ($n$) in the array, leave array as is.
  This is because performing ($n$) rotations simply repositions the array elements back into their initial positions
 **after moving them around for no damn reason**.

- If $K$ exceeds $n$, there is some circularity involved. Simply perform only the extra amount of rotations required
 (determined by the difference between $K$ and $n$.
"""

from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if k > n: k = k % n
    if 0 < k < 3000:
        for _ in range(k):
            i = n - 1
            temp = nums[i]
            while i != -1:
                nums[i] = nums[i - 1]
                i -= 1
            nums[0] = temp
    elif k > 3000:
        nums[n - k:], nums[:n - k] = nums[:n - k], nums[n - k:]



if __name__ == "__main__":
    l1 = [1,2,3,4,5,6,7]
    l2 = [-1,-100,3,99]
    l3 = [1,2,3,4,5,6]

    print(l1); rotate(l1, 3); print(" -> ", l1, "\n")
    print(l2); rotate(l2, 2); print(" -> ", l2, "\n")
    print(l3); rotate(l3, 1); print(" -> ", l3, "\n")
