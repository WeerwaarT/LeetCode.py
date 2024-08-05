# 2603. 收集树中金币
# https://leetcode.cn/problems/collect-coins-in-a-tree/
import collections
from typing import List


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n, total = len(coins), sum(coins)
        if total < 2 or n < 6:
            return 0

        my_edges = collections.defaultdict(set)
        degrees = [0] * n
        for edge in edges:
            degrees[edge[0]] += 1
            degrees[edge[1]] += 1
            my_edges[edge[0]].add(edge[1])
            my_edges[edge[1]].add(edge[0])

        queue = collections.deque([j for j in range(n) if degrees[j] == 1 and coins[j] == 0])
        while queue:
            cur = queue.popleft()
            degrees[cur] = 0
            neighbour = my_edges[cur].pop()
            my_edges.pop(cur)
            my_edges[neighbour].discard(cur)
            degrees[neighbour] -= 1
            if degrees[neighbour] == 1 and coins[neighbour] == 0:
                queue.append(neighbour)

        def f():
            for i in [j for j in range(n) if degrees[j] == 1]:
                if degrees[i] == 0:
                    return 0

                degrees[i] = 0
                neighbour = my_edges[i].pop()
                my_edges.pop(i)
                my_edges[neighbour].discard(i)
                coins[neighbour] += coins[i]
                coins[i] = 0
                degrees[neighbour] -= 1

        f()
        f()
        return sum([len(v) for v in my_edges.values()])
        # index = next((i for i, v in enumerate(coins) if v != 0), None)
        # queue = collections.deque([index])
        # count = 0
        # step = 0
        # while queue:
        #     cur = queue.popleft()
        #     count += coins[cur]
        #     if count == total:
        #         return 2 * step
        #
        #     for neighbour in my_edges[cur]:
        #         my_edges[neighbour].discard(cur)
        #         step += 1
        #         queue.append(neighbour)

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/collect-coins-in-a-tree/solutions/2451073/shou-ji-shu-zhong-jin-bi-by-leetcode-sol-kaah/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = collections.defaultdict(list)
        degree = [0] * n

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            degree[x] += 1
            degree[y] += 1

        rest = n
        # 删除树中所有无金币的叶子节点，直到树中所有的叶子节点都是含有金币的
        q = collections.deque(i for i in range(n) if degree[i] == 1 and coins[i] == 0)
        while q:
            u = q.popleft()
            degree[u] -= 1
            rest -= 1
            for v in g[u]:
                degree[v] -= 1
                if degree[v] == 1 and coins[v] == 0:
                    q.append(v)

        # 删除树中所有的叶子节点, 连续删除2次
        for _ in range(2):
            q = collections.deque(i for i in range(n) if degree[i] == 1)
            while q:
                u = q.popleft()
                degree[u] -= 1
                rest -= 1
                for v in g[u]:
                    degree[v] -= 1

        return 0 if rest == 0 else (rest - 1) * 2


    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        deg = list(map(len, g))

        left_edges = n - 1
        q = []
        for i, (d, c) in enumerate(zip(deg, coins)):
            if d == 1 and c == 0:
                q.append(i)
        while q:
            left_edges -= 1
            for y in g[q.pop()]:
                deg[y] -= 1
                if deg[y] == 1 and coins[y] == 0:
                    q.append(y)

        for i, (d, c) in enumerate(zip(deg, coins)):
            if d == 1 and c:
                q.append(i)
        left_edges -= len(q)
        for x in q:
            for y in g[x]:
                deg[y] -= 1
                if deg[y] == 1:
                    left_edges -= 1
        return max(left_edges * 2, 0)


print(Solution().collectTheCoins([1,1,1,1,1,1,0,0],
                                 [[0,1],[1,2],[1,3],[2,4],[2,5],[4,6],[3,7]]))