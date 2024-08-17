from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        m_ = m - 1
        ans = 0
        depths = [[0 for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            visited[i][-1] = True

        def dfs(row: int, column: int) -> int:
            if visited[row][column]:
                return depths[row][column]

            max_depth = 0
            if row != 0 and grid[row - 1][column + 1] > grid[row][column]:
                max_depth = max(max_depth, dfs(row - 1, column + 1) + 1)

            if grid[row][column + 1] > grid[row][column]:
                max_depth = max(max_depth, dfs(row, column + 1) + 1)

            if row != m_ and grid[row + 1][column + 1] > grid[row][column]:
                max_depth = max(max_depth, dfs(row + 1, column + 1) + 1)

            visited[row][column] = True
            depths[row][column] = max_depth
            return max_depth

        for i in range(m):
            ans = max(ans, dfs(i, 0))

        return ans

    # def maxMoves(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     vis = [-1] * m
    #     q = range(m)
    #     for j in range(n - 1):
    #         tmp = q
    #         q = []
    #         for i in tmp:
    #             for k in i - 1, i, i + 1:
    #                 if 0 <= k < m and vis[k] != j and grid[k][j + 1] > grid[i][j]:
    #                     vis[k] = j
    #                     q.append(k)
    #         if not q:
    #             return j
    #     return n - 1


if __name__ == '__main__':
    print(Solution().maxMoves([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]))
    print(Solution().maxMoves([[3, 2, 4], [2, 1, 9], [1, 1, 7]]))
