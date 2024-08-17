# 309. 买卖股票的最佳时机含冷冻期
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        dp = [[0] * n] * 3
        dp[0][0] -= prices[0]
        dp[1][1] = prices[1] - prices[0]


if __name__ == '__main__':
    print(Solution().maxProfit([1, 2, 4, 3, 5, 6]))
