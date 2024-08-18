# 746. 使用最小花费爬楼梯
# https://leetcode.cn/problems/min-cost-climbing-stairs/
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        pre_pre, pre = cost[0], cost[1]

        for i in range(2, n):
            pre_pre, pre = pre, min(pre_pre, pre) + cost[i]

        return min(pre_pre, pre)

    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     n = len(cost)
    #     f = [0]*(n+1)
    #     for i in range(2,n+1):
    #         f[i] = min(f[i-1]+cost[i-1],f[i-2]+cost[i-2])
    #     return f[-1]