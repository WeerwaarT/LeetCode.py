# 207. 课程表
# https://leetcode.cn/problems/course-schedule/
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 作者：力扣官方题解
        # 链接：https://leetcode.cn/problems/course-schedule/solutions/359392/ke-cheng-biao-by-leetcode-solution/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            result.append(u)

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 作者：力扣官方题解
        # 链接：https://leetcode.cn/problems/course-schedule/solutions/359392/ke-cheng-biao-by-leetcode-solution/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses