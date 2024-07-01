from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        left = right = -1
        n = len(nums)
        prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        for i, num in enumerate(nums):
            if num in prime:
                left = i
                break

        for i in range(n - 1, -1, -1):
            if nums[i] in prime:
                right = i
                break

        return right - left
