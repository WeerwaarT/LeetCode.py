from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        max_step = sum(row.count(0) for row in grid) + 1
        