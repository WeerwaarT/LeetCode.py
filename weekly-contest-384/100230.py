from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        pos = []
        col_max = [-2] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    pos.append((i, j))
                else:
                    col_max[j] = max(col_max[j], matrix[i][j])

        for i, j in pos:
            matrix[i][j] = col_max[j]

        return matrix