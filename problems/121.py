# 121. 买卖股票的最佳时机
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur = prices[0]
        for p in prices:
            if p > cur:
                profit = max(profit, p - cur)
            else:
                cur = p

        return profit