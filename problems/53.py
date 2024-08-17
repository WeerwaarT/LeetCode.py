# 53. 最大子数组和
# https://leetcode.cn/problems/maximum-subarray/description/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_sum = nums[0]
        acc = 0
        for num in nums:
            acc += num
            max_sum = max(max_sum, acc)
            acc = max(0, acc)

        return max_sum

    # def maxSubArray(self, nums: List[int]) -> int:
    #     numsSum = [0 for i in range(len(nums))]
    #     numsSum[0] = nums[0]
    #
    #     for i in range(1, len(nums)):
    #         numsSum[i] = max(nums[i], nums[i] + numsSum[i - 1])
    #     return max(numsSum)