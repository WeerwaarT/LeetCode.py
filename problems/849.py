# 849. 到最近的人的最大距离
# https://leetcode.cn/problems/maximize-distance-to-closest-person/
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        head = 0
        tail = n - 1

        while not seats[head]: head += 1
        while not seats[tail]: tail -= 1
        tail = n - 1 - tail

        i = head + 1
        cur_dist = 1
        max_dist = 2 * max(head, tail)
        while i < n:
            if seats[i]:
                max_dist = max(max_dist, cur_dist)
                cur_dist = 0

            cur_dist += 1
            i += 1

        return max_dist // 2