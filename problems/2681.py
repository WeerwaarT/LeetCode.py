# 2681. 英雄的力量
# https://leetcode.cn/problems/power-of-heroes/
from typing import List


class Solution:
    # 我自己想的，花了好久，速度慢了一点点，之前还有一版也是对的不过超时了
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        mod = pow(10, 9) + 7
        squared_nums = [pow(x, 2) % mod for x in nums]

        total_power = sum(a * b for a, b in zip(squared_nums, nums)) % mod
        multiplier = 0
        for i in range(1, len(nums)):
            multiplier = (2 * multiplier + nums[i - 1]) % mod
            total_power += (multiplier * squared_nums[i]) % mod

        return total_power % mod

    # 速度最优的，思路其实和我的差不多
    def sumOfPower_1(self, nums: List[int]) -> int:
        nums.sort()
        mod = pow(10, 9) + 7

        total_power = 0
        multiplier = 0
        for n in nums:
            total_power = (total_power + (n ** 2) * (multiplier + n)) % mod
            multiplier = (2 * multiplier + n) % mod

        return total_power
