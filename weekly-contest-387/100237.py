from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        my_grid = [[0] * n] * m
        my_grid[0][0] = grid[0][0]
        count = 1 if grid[0][0] <= k else 0
        for i in range(1, n):
            my_grid[0][i] = grid[0][i] + my_grid[0][i - 1]
            count += 1 if my_grid[0][i] <= k else 0

        for i in range(1, m):
            my_grid[i][0] = grid[i][0] + my_grid[i - 1][0]
            count += 1 if my_grid[i][0] <= k else 0

        for i in range(1, m):
            sub_sum = grid[i][0]
            for j in range(1, n):
                sub_sum += grid[i][j]
                my_grid[i][j] = my_grid[i - 1][j] + sub_sum
                count += 1 if my_grid[i][j] <= k else 0

        return count

    # 优秀啊，优秀QAQ
    # def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
    #     m, n = len(grid), len(grid[0])
    #     pres = [[0] * (n+1) for _ in range(m+1)]
    #     ans = 0
    #     for i, row in enumerate(grid):
    #         for j, x in enumerate(row):
    #             pres[i+1][j+1] = pres[i+1][j] + pres[i][j+1] - pres[i][j] + x
    #             ans += pres[i+1][j+1] <= k
    #     return ans


if __name__ == '__main__':
    print(Solution().countSubmatrices([[9, 9, 3], [1, 1, 7], [8, 4, 6], [10, 3, 2], [2, 3, 3]], 49))
