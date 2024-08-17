# 33. 搜索旋转排序数组
# https://leetcode.cn/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:  # head on right or unrotated, check left
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # head on left, check right
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        if nums[left] == target:
            return left

        if nums[right] == target:
            return right

        return -1