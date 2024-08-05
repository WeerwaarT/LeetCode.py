# 2596. 检查骑士巡视方案
# https://leetcode.cn/problems/check-knight-tour-configuration/
from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        max_num = n * n - 1
        directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        def dfs(num: int, row : int, col: int) -> bool:
            if num == max_num:
                return True

            for move in [(row + dr, col + dc) for dr, dc in directions if 0 <= row + dr < n and 0 <= col + dc < n]:
                if grid[move[0]][move[1]] == num + 1:
                    return dfs(num + 1, move[0], move[1])

            return False

        return dfs(0, 0, 0) if grid[0][0] == 0 else False


print(Solution().checkValidGrid([[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]))