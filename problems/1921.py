# 1921. 消灭怪物的最大数量
# https://leetcode.cn/problems/eliminate-maximum-number-of-monsters/
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        order = sorted([dist[i] / speed[i] for i in range(len(dist))])
        count = 0
        for monster in order:
            if monster <= count:
                break

            count += 1

        return count