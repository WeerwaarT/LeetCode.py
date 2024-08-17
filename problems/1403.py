from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        _sum = sum(nums)
        pivot = 0
        __sum = 0

        while True:
            __sum += nums[pivot]
            _sum -= nums[pivot]
            pivot += 1
            if __sum > _sum:
                break

        return nums[0:pivot]
