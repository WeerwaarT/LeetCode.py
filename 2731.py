# 2731. 移动机器人
# https://leetcode.cn/problems/movement-of-robots/
from typing import List


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)
        for i in range(n):
            if s[i] == 'L':
                nums[i] -= d
            else:
                nums[i] += d

        nums.sort()
        total_distance = 0
        mod = 10 ** 9 + 7
        for i in range(n // 2):
            total_distance += (nums[-i - 1] - nums[i]) * (n - 1)
            n -= 2

        return total_distance % 1_000_000_007

    # def sumDistance(self, nums: List[int], s: str, d: int) -> int:
    #     n = len(nums)
    #     for i in range(n):
    #         if s[i] == 'L':
    #             nums[i] -= d
    #         else:
    #             nums[i] += d
    #
    #     nums.sort()
    #     ans = s = 0
    #     for i, x in enumerate(nums):
    #         ans += i * x - s
    #         s += x
    #     return ans % (10 ** 9 + 7)