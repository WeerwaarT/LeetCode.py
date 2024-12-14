from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:    # dfs
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(x: int, y: int) -> None:
            if not (0 <= x < m and 0 <= y < n and board[x][y] == 'O'):
                return

            board[x][y] = 'A'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        m, n = len(board), len(board[0])
        if min(m, n) < 3:
            return

        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'O':
                    dfs(i, j)

        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

        return

    def solve_union_find(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for line in board:
            print(line)

        m, n = len(board), len(board[0])
        if min(m, n) < 3:
            return

        parents = [i for i in range(m * n + 1)]
        sizes = [1] * (m * n + 1)
        dummy = m * n
        def find(node: int) -> int:
            # path compression
            # if parents[node] != node:
            #     parents[node] = find(parents[node])
            # return parents[node]
            while parents[node] != node:
                node = parents[node]

            return node

        def union(node1: int, node2: int) -> None:
            root1 = find(node1)
            root2 = find(node2)
            if root1 == root2:
                return

            if sizes[root1] < sizes[root2]:
                parents[root1] = root2  # parents[node1] = node2 <- this is wrong
                sizes[root2] += sizes[root1]
            else:
                parents[root2] = root1
                sizes[root1] += sizes[root2]

        def is_connected(node1: int, node2: int) -> bool:
            return find(node1) == find(node2)

        # could be used to simplify code
        # def nd(i: int, j: int) -> int:
        #     return i * n + j

        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'O':
                    union(i * n + j, dummy) # not i * m + j

        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    union(i * n + j, dummy)

        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 'O':
                    continue

                node = i * n + j
                if board[i + 1][j] == 'O':
                    union(node, i * n + n + j)

                if board[i][j + 1] == 'O':
                    union(node, i * n + j + 1)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if is_connected(i * n + j, dummy):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

        print('--------------------------')
        for line in board:
            print(line)


if __name__ == '__main__':
    Solution().solve_union_find([["O","X","X","O","X"],
                                 ["X","O","O","X","O"],
                                 ["X","O","X","O","X"],
                                 ["O","X","O","O","O"],
                                 ["X","X","O","X","O"]])