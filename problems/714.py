# 714. 买卖股票的最佳时机含手续费
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        cur_min, cur_max = prices[0] + fee, prices[0]
        for price in prices:
            if (price + fee) < cur_max or (price + fee) < cur_min:
                profit += max(0, cur_max - cur_min)
                cur_min = price + fee
                cur_max = price

            cur_max = max(cur_max, price)

        if (prices[-1] + fee) >= cur_max:
            profit += max(0, cur_max - cur_min)

        return profit


if __name__ == '__main__':
    print(Solution().maxProfit([4,5,2,4,3,3,1,2,5,4], 1))