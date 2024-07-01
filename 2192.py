import collections
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        all_ancestor = collections.defaultdict(set)
        for f, t in edges:
            all_ancestor[t].add(f)

        visited = [False] * n

        def dfs(node: int) -> None:
            if visited[node]:
                return

            visited[node] = True
            for ancestor in list(all_ancestor[node]):
                dfs(ancestor)
                all_ancestor[node].update(all_ancestor[ancestor])

        for i in range(n):
            dfs(i)

        ans = []
        for i in range(n):
            ans.append(sorted(all_ancestor[i]))

        return ans
