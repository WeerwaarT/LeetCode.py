# 1465. 切割后面积最大的蛋糕
# https://leetcode.cn/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()

        max_width, max_height = -1, -1
        for i in range(1, len(horizontalCuts)):
            max_height = max(max_height, horizontalCuts[i] - horizontalCuts[i - 1])

        for i in range(1, len(verticalCuts)):
            max_width = max(max_width, verticalCuts[i] - verticalCuts[i - 1])

        return max_height * max_width % (10 ** 9 + 7)


if __name__ == '__main__':
    print(Solution().maxArea(5, 4, [1, 2, 4], [1, 3]) == 4)
    print(Solution().maxArea(5, 4, [3, 1], [1]) == 6)
