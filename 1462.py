# 1462. 课程表 IV
# https://leetcode.cn/problems/course-schedule-iv/
import collections
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        my_dict = collections.defaultdict(set)
        for prerequisite in prerequisites:
            my_dict[prerequisite[1]].add(prerequisite[0])

        ans = []
        for query in queries:
            s = my_dict[query[1]]
            is_prerequisite = False
            while s:
                if query[0] in s:
                    is_prerequisite = True
                    break

                s = set(u for i in s for u in my_dict[i])

            ans.append(is_prerequisite)

        return ans

    