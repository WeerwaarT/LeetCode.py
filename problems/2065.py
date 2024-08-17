from collections import defaultdict
from typing import List


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        g = defaultdict(list)
        for x, y, z in edges:
            g[x].append((y, z))
            g[y].append((x, z))

        visited = {0}
        ans = 0

        def dfs(u: int, time: int, value: int) -> None:
            if u == 0:
                nonlocal ans
                ans = max(ans, value)
            for v, dist in g[u]:
                if time + dist <= maxTime:
                    if v not in visited:
                        visited.add(v)
                        dfs(v, time + dist, value + values[v])
                        visited.discard(v)
                    else:
                        dfs(v, time + dist, value)

        dfs(0, 0, values[0])
        return ans

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/maximum-path-quality-of-a-graph/solutions/1092073/zui-da-hua-yi-zhang-tu-zhong-de-lu-jing-yim5i/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == '__main__':
    print(Solution().maximalPathQuality([0, 32, 10, 43], [[0, 1, 10], [1, 2, 15], [0, 3, 10]], 49))
