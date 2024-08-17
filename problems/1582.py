from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        row = [0] * m
        column = [0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    row[i] += 1
                    column[j] += 1

        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] and row[i] == 1 and column[j] == 1:
                    count += 1

        return count
