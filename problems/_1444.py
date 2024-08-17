# 1444. 切披萨的方案数
# https://leetcode.cn/problems/number-of-ways-of-cutting-a-pizza/
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        mod = 10 ** 9 + 7
        row = len(pizza)
        col = len(pizza[0])

        