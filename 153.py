# 153. 寻找旋转排序数组中的最小值
# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        n = len(nums)
        mid = n // 2 - 1

        if nums[mid] < nums[-1]:
            return self.findMin(nums[0:mid + 1])
        else:
            return self.findMin(nums[mid + 1:])