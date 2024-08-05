# 136. 只出现一次的数字
# https://leetcode.cn/problems/single-number/
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num

        return ans

