# 463. 岛屿的周长
# https://leetcode.cn/problems/island-perimeter/
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False for _ in row] for row in grid]

        def dfs(x: int, y: int) -> int:
            if not ((0 <= x < col) and (0 <= y < row)) or grid[y][x] == 0:
                return 1

            if visited[y][x]:
                return 0

            visited[y][x] = True
            total_perimeter = 0
            total_perimeter += dfs(x - 1, y)
            total_perimeter += dfs(x + 1, y)
            total_perimeter += dfs(x, y + 1)
            total_perimeter += dfs(x, y - 1)
            return total_perimeter

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return dfs(j, i)

    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    #     length = len(grid)
    #     width = len(grid[0])
    #     prm = 0
    #     for i in range(length):
    #         for j in range(width):
    #             if grid[i][j] == 1:
    #                 if j == 0 or grid[i][j - 1] == 0:
    #                     prm += 1
    #                 if i == 0 or grid[i - 1][j] == 0:
    #                     prm += 1
    #     return prm * 2
