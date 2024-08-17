# 2316. 统计无向图中无法互相到达点对数
# https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/
import collections
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        all_edges = collections.defaultdict(list)
        for edge_a, edge_b in edges:
            all_edges[edge_a].append(edge_b)
            all_edges[edge_b].append(edge_a)

        count = 0
        for i in range(n):
            if visited[i]:
                continue

            if len(all_edges[i]) == 0:
                count += n - 1
                continue

            queue = collections.deque()
            size = 0
            queue.append(i)
            while queue:
                node = queue.popleft()
                if visited[node]:
                    continue

                size += 1
                queue.extend(all_edges[node])
                visited[node] = True

            count += size * (n - size)

        return count // 2

    # def countPairs(self, n: int, edges: List[List[int]]) -> int:
    #     graph_sizes = []
    #     visited = [False] * n
    #     all_edges = collections.defaultdict(list)
    #     for edge_a, edge_b in edges:
    #         all_edges[edge_a].append(edge_b)
    #         all_edges[edge_b].append(edge_a)
    #
    #     for i in range(n):
    #         if visited[i]:
    #             continue
    #
    #         if len(all_edges[i]) == 0:
    #             graph_sizes.append(1)
    #             continue
    #
    #         queue = collections.deque()
    #         size = 0
    #         queue.append(i)
    #         while queue:
    #             node = queue.popleft()
    #             if visited[node]:
    #                 continue
    #
    #             size += 1
    #             queue.extend(all_edges[node])
    #             visited[node] = True
    #
    #         graph_sizes.append(size)
    #
    #     count = 0
    #     graph_count = len(graph_sizes)
    #     for i in range(graph_count):
    #         for j in range(i + 1, graph_count):
    #             count += graph_sizes[i] * graph_sizes[j]
    #
    #     return count


if __name__ == '__main__':
    print(Solution().countPairs(3, [[0, 1], [0, 2], [1, 2]]))
    print(Solution().countPairs(7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]))
