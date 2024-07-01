import collections
from typing import List


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        Y_count = collections.Counter()
        non_Y_count = collections.Counter()
        n = len(grid)
        mid = n // 2

        def isY(x: int, y: int) -> bool:
            if x <= mid and (x == y or y == n - 1 - x):
                return True

            if x > mid and y == mid:
                return True

            return False

        for i in range(n):
            for j in range(n):
                if isY(i, j):
                    Y_count[grid[i][j]] += 1
                else:
                    non_Y_count[grid[i][j]] += 1

        min_operations = float('inf')
        for Y_value in [0, 1, 2]:
            for non_Y_value in [0, 1, 2]:
                if Y_value != non_Y_value:
                    # 计算将Y部分变为Y_value的操作次数
                    Y_operations = sum(count for value, count in Y_count.items() if value != Y_value)
                    # 计算将非Y部分变为non_Y_value的操作次数
                    non_Y_operations = sum(count for value, count in non_Y_count.items() if value != non_Y_value)
                    # 更新最小操作次数
                    min_operations = min(min_operations, Y_operations + non_Y_operations)

        return min_operations


if __name__ == '__main__':
    print(Solution().minimumOperationsToWriteY([[1, 2, 2], [1, 1, 0], [0, 1, 0]]))
    print(Solution().minimumOperationsToWriteY(
        [[0, 1, 0, 1, 0], [2, 1, 0, 1, 2], [2, 2, 2, 0, 1], [2, 2, 2, 2, 2], [2, 1, 2, 2, 2]]))
