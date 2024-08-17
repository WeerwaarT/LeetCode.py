# 1749. 任意子数组和的绝对值的最大值
# https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/
from itertools import accumulate
from typing import List


class Solution:
    # 前缀和
    # 太优雅了，我根本想不出来
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s = list(accumulate(nums, initial=0))  # nums 的前缀和
        return max(s) - min(s)

    # 动态规划我也不会
    # def maxAbsoluteSum(self, nums: List[int]) -> int:
    #     ans = f_max = f_min = 0
    #     for x in nums:
    #         f_max = max(f_max, 0) + x
    #         f_min = min(f_min, 0) + x
    #         ans = max(ans, f_max, -f_min)
    #     return ans

    # def maxAbsoluteSum(self, nums: List[int]) -> int:
    #     positiveMax, negativeMin = 0, 0
    #     positiveSum, negativeSum = 0, 0
    #     for n in nums:
    #         positiveSum += n
    #         positiveMax = max(positiveMax, positiveSum)
    #         positiveSum = max(0, positiveSum)

    #         negativeSum += n
    #         negativeMin = min(negativeMin, negativeSum)
    #         negativeSum = min(0, negativeSum)

    #     return max(positiveMax, -negativeMin)
    