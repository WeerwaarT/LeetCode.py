# 1572. 矩阵对角线元素的和
# https://leetcode.cn/problems/matrix-diagonal-sum/
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)

        if n == 1:
            return mat[0][0]

        total = 0 if n % 2 == 0 else -mat[n // 2][n // 2]
        for i in range(n):
            n -= 1
            total += mat[i][i]
            total += mat[i][n]

        return total