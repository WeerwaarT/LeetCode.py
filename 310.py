import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        in_degrees = [0] * n
        graph = collections.defaultdict(list)
        for a, b in edges:
            in_degrees[a] += 1
            in_degrees[b] += 1
            graph[a].append(b)
            graph[b].append(a)

        q = [i for i, d in enumerate(in_degrees) if d == 1]
        while n > 2:
            temp = []
            for a in q:
                n -= 1
                for b in graph[a]:
                    in_degrees[b] -= 1
                    if in_degrees[b] == 1:
                        temp.append(b)

            q = temp
        return q


if __name__ == '__main__':
    print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
