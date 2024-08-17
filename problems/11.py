# 11. 盛最多水的容器
# https://leetcode.cn/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area = 0
        left, right = 0, n - 1

        while left < right:
            if height[left] < height[right]:
                area = max(area, height[left] * (right - left))
                left += 1
            else:
                area = max(area, height[right] * (right - left))
                right -= 1

        return area


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(Solution().maxArea([1, 1]))
