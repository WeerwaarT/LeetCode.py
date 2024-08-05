# 1267. 统计参与通信的服务器
# https://leetcode.cn/problems/count-servers-that-communicate/
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rows = [False] * m
        cols = [False] * n

        for i in range(m):
            for j in range(n):
                if cols[j]:
                    continue

                if grid[i][j]:
                    if not rows[i]:
                        for p in range(0, n):
                            if p == j: continue
                            if grid[i][p]:
                                rows[i] = True
                                break

                    if not cols[j]:
                        for q in range(0, m):
                            if q == i: continue
                            if grid[q][j]:
                                cols[j] = True
                                break

                if rows[i]:
                    break

                if not cols[j]:
                        grid[i][j] = 0

        return sum(sum(row) for row in grid)