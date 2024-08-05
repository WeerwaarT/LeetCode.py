# 1222. 可以攻击国王的皇后
# https://leetcode.cn/problems/queens-that-can-attack-the-king/
from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        mv = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
        for x, y in mv:
            X, Y = king
            while 0 <= (X + x) < 8 and 0 <= (Y + y) < 8:
                X += x
                Y += y
                if [X, Y] in queens:
                    ans.append([X, Y])
                    break

        return ans
