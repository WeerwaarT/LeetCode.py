# 123. 买卖股票的最佳时机 III
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/
from typing import List, Tuple


class Solution:
    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/solutions/552695/mai-mai-gu-piao-de-zui-jia-shi-ji-iii-by-wrnt/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2

    # def maxProfit(self, prices: List[int]) -> int:
    #     buy1, buy2 = prices[0], prices[0]
    #     sell1, sell2 = 0, 0
    #     for i in range(1, len(prices)):
    #         if prices[i] < prices[i-1]:
    #             price = prices[i]
    #             if price < buy1:
    #                 buy1 = price
    #             if price - sell1 < buy2:
    #                 buy2 = price - sell1
    #         elif prices[i] > prices[i-1]:
    #             price = prices[i]
    #             if price - buy1 > sell1:
    #                 sell1 = price - buy1
    #             if price - buy2 > sell2:
    #                 sell2 = price - buy2
    #     return sell2


if __name__ == '__main__':
    print(Solution().maxProfit([6,1,3,2,4,7]))