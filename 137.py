# 137. 只出现一次的数字 II
# https://leetcode.cn/problems/single-number-ii/
import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3*sum(set(nums))-sum(nums))//2

    def singleNumber(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        ans = [num for num, occ in freq.items() if occ == 1][0]
        return ans

    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            b = (b ^ num) & ~a
            a = (a ^ num) & ~b
        return b