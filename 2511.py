# 2511. 最多可以摧毁的敌人城堡数目
# https://leetcode.cn/problems/maximum-enemy-forts-that-can-be-captured/
from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        routes = []
        for i, fort in enumerate(forts):
            if fort > 0:
                routes.append((True, i))
            elif fort < 0:
                routes.append((False, i))

        captured = 0
        for i in range(len(routes) - 1):
            if routes[i][0] ^ routes[i + 1][0]:
                captured = max(captured, routes[i + 1][1] - routes[i][1] - 1)

        return captured