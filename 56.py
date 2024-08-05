# 56. 合并区间
# https://leetcode.cn/problems/merge-intervals/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for interval in intervals:
            if interval[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans.append(interval)

        return ans


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))