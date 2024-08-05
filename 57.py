# 57. 插入区间
# https://leetcode.cn/problems/insert-interval/
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        intervals.append(newInterval)
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        i = 1
        while i < n:
            if intervals[i][0] <= ans[-1][1]:
                while i < n and intervals[i][0] <= ans[-1][1]:
                    ans[-1][1] = max(ans[-1][1], intervals[i][1])
                    i += 1

                break
            else:
                ans.append(intervals[i])

            i += 1

        ans += intervals[i:]
        return ans


print(Solution().insert([[1,5]], [2,3]))