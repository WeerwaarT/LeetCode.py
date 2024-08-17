# 2562. 找出数组的串联值
# https://leetcode.cn/problems/find-the-array-concatenation-value/
from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        total = 0
        while left < right:
            total += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1

        if left == right:
            total += nums[left]

        return total

    # def findTheArrayConcVal(self, nums: List[int]) -> int:
    #     ans = 0
    #     i = 0
    #     j = len(nums) - 1
    #     while i < j:
    #         x = nums[i]
    #         y = nums[j]
    #         while y:
    #             x *= 10
    #             y //= 10
    #         ans += x + nums[j]
    #         i += 1
    #         j -= 1
    #
    #     if i == j:
    #         ans += nums[i]
    #
    #     return ans