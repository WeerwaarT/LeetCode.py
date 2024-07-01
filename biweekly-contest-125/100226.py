import collections
from typing import List


class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        path = collections.defaultdict(list)
        for a, b, weight in edges:
            path[a].append((b, weight))
            path[b].append((a, weight))

        ans = [0] * n
        for a in range(n):
            queue_c = path[a]
            visited_a = [False] * n
            visited_a[a] = True
            while queue_c:
                temp_c = []
                for c, d_ac in queue_c:
                    if visited_a[c]:
                        continue

                    visited_a[c] = True
                    visited_c = visited_a
                    queue_b = path[c]
                    temp_c.extend(queue_b)
                    while queue_b:
                        temp_b = []
                        for b, d_cb in queue_b:
                            if visited_c[b]:
                                continue

                            visited_c = True
                            d_ab = d_ac + d_cb
                            temp_b.append((b, d_ab))
                            if a < b and d_ac % signalSpeed == 0 and d_cb % signalSpeed == 0:
                                ans[c] += 1

                        queue_b = temp_b

                queue_c = temp_c

        return ans


if __name__ == '__main__':
    print(Solution().countPairsOfConnectableServers([[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]], 1))
    print(Solution().countPairsOfConnectableServers([[0, 6, 3], [6, 5, 3], [0, 3, 1], [3, 2, 7], [3, 1, 6], [3, 4, 2]],
                                                    3))
