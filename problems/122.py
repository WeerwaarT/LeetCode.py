# 122. 买卖股票的最佳时机 II
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur_min = cur_max = prices[0]
        for price in prices:
            if price < cur_max:
                profit += cur_max - cur_min
                cur_min = price

            cur_max = price

        if prices[-1] == cur_max:
            profit += max(0, cur_max - cur_min)

        return profit


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))