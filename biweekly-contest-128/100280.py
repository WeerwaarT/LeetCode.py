from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        xs = sorted(x for x, _ in points)
        right = xs[0] + w
        count = 1
        for x in xs:
            if x <= right:
                continue

            right = x + w
            count += 1

        return count
