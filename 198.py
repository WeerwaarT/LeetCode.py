# 198. 打家劫舍
# https://leetcode.cn/problems/house-robber/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        g0, g1 = 0, 0

        for i in range(n):
            g0, g1 = g1, max(g1, g0 + nums[i])

        return max(g0, g1)

    # def rob(self, nums: List[int]) -> int:
    #     # a robber will either rob a house or not
    #     # if they choose to rob house i, they find maximum of
    #     # dp[i-2] + nums[i] money, since they cannot rob nums[i-1].
    #     # so dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    #     if (len(nums) == 1):
    #         return nums[0]
    #     dp = [0] * len(nums)
    #     dp[0] = nums[0]
    #     dp[1] = max(dp[0], nums[1])
    #
    #     for i in range(2, len(nums)):
    #         dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    #
    #     return dp[-1]