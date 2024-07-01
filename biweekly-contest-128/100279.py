import collections
import heapq
from typing import List


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        ans = [-1] * n
        ans[0] = 0
        graph = collections.defaultdict(dict)
        for u, v, length in edges:
            if v in graph[u]:
                graph[u][v] = graph[v][u] = min(length, graph[u][v])
            else:
                graph[u][v] = graph[v][u] = length

        priority_queue = [(0, 0)]
        visited = [False] * n
        while priority_queue:
            cur_t, node = heapq.heappop(priority_queue)
            if visited[node] and cur_t >= ans[node]:
                continue

            visited[node] = True
            ans[node] = cur_t
            for v, length in graph[node].items():
                new_t = cur_t + length
                if new_t >= disappear[v]:
                    continue

                if not visited[v] or cur_t + length < ans[v]:
                    heapq.heappush(priority_queue, (new_t, v))

        return ans
