# 260. 只出现一次的数字 III
# https://leetcode.cn/problems/single-number-iii/
from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [num for num, occ in freq.items() if occ == 1]
