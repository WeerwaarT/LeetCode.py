# [LCP 06. 拿硬币](https://leetcode.cn/problems/na-ying-bi/)
from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum([(coin + 1) // 2 for coin in coins])