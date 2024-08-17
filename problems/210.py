# 210. 课程表 II
# https://leetcode.cn/problems/course-schedule-ii/
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(list)
        degree_in = [0] * numCourses
        for prerequisite in prerequisites:
            edges[prerequisite[1]].append(prerequisite[0])
            degree_in[prerequisite[0]] += 1

        result = []
        queue = collections.deque([course for course in range(numCourses) if degree_in[course] == 0])

        while queue:
            course = queue.popleft()
            result.append(course)
            for c in edges[course]:
                degree_in[c] -= 1
                if degree_in[c] == 0:
                    queue.append(c)

        if len(result) != numCourses:
            return []
        else:
            return result
