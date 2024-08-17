# 740. 删除并获得点数
# https://leetcode.cn/problems/delete-and-earn/
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + num

        p0, p1 = 0, 0
        for key in sorted(d.keys()):
            p0, p1 = p1, max(p1, p0 + d[key])

        return max(p0, p1)
