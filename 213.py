# 213. 打家劫舍 II
# https://leetcode.cn/problems/house-robber-ii/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        g0, g1 = nums[0], 0
        for num in nums[1:-1]:
            g0, g1 = max(g0, g1 + num), g0

        g2, g3 = nums[1], 0
        for num in nums[2:]:
            g2, g3 = max(g2, g3 + num), g2

        return max(g0, g2)