# 188. 买卖股票的最佳时机 IV
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/
from typing import List


class Solution:
    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/solutions/537731/mai-mai-gu-piao-de-zui-jia-shi-ji-iv-by-8xtkp/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def maxProfit(self, k: int, prices: List[int]) -> int:
        from math import sin
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]

        buy[0][0], sell[0][0] = -prices[0], 0
        for i in range(1, k + 1):
            buy[0][i] = sell[0][i] = float("-inf")

        for i in range(1, n):
            buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i]);

        return max(sell[n - 1])

    # 最快的
    # def maxProfit(self, k: int, prices: List[int]) -> int:
    #     if not prices:
    #         return 0
    #
    #     n = len(prices)
    #     # 二分查找的上下界
    #     left, right = 1, max(prices)
    #     # 存储答案，如果值为 -1 表示二分查找失败
    #     ans = -1
    #
    #     while left <= right:
    #         # 二分得到当前的斜率（手续费）
    #         c = (left + right) // 2
    #
    #         # 使用与 714 题相同的动态规划方法求解出最大收益以及对应的交易次数
    #         buyCount = sellCount = 0
    #         buy, sell = -prices[0], 0
    #
    #         for i in range(1, n):
    #             if sell - prices[i] >= buy:
    #                 buy = sell - prices[i]
    #                 buyCount = sellCount
    #             if buy + prices[i] - c >= sell:
    #                 sell = buy + prices[i] - c
    #                 sellCount = buyCount + 1
    #
    #         # 如果交易次数大于等于 k，那么可以更新答案
    #         # 这里即使交易次数严格大于 k，更新答案也没有关系，因为总能二分到等于 k 的
    #         if sellCount >= k:
    #             # 别忘了加上 kc
    #             ans = sell + k * c
    #             left = c + 1
    #         else:
    #             right = c - 1
    #
    #     # 如果二分查找失败，说明交易次数的限制不是瓶颈
    #     # 可以看作交易次数无限，直接使用贪心方法得到答案
    #     if ans == -1:
    #         ans = sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))
    #
    #     return ans
