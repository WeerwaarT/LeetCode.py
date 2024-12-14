from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def idx(i: int, j: int) -> int:
            return i * n + j

        sizes = [1] * (m * n)
        parents = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    parents.append(idx(i, j))
                else:
                    parents.append(-1)

        def find(node: int) -> int:
            if parents[node] != node:
                parents[node] = find(parents[node])

            return parents[node]

        def union(node1: int, node2: int) -> None:
            root1 = find(node1)
            root2 = find(node2)
            if root1 == root2:
                return

            if sizes[root1] < sizes[root2]:
                parents[root1] = root2
                sizes[root2] += sizes[root1]
            else:
                parents[root2] = root1
                sizes[root1] += sizes[root2]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if i + 1 < m and grid[i + 1][j] == '1':
                        union(idx(i, j), idx(i + 1, j))
                    if j + 1 < n and grid[i][j + 1] == '1':
                        union(idx(i, j), idx(i, j + 1))

        count = 0
        for i, p in enumerate(parents):
            if p == i:
                count += 1

        return count
