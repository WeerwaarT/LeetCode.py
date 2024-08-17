# LCP 50. 宝石补给
# https://leetcode.cn/problems/WHnhjV/
from typing import List


class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for x, y in operations:
            away = gem[x] // 2
            gem[y] += away
            gem[x] -= away

        return max(gem) - min(gem)