from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)

    def _maxProduct(self, nums: List[int]) -> int:
        a, b = nums[0], nums[1]
        if a < b:
            a, b = b, a
        for i in range(2, len(nums)):
            num = nums[i]
            if num > a:
                a, b = num, a
            elif num > b:
                b = num
        return (a - 1) * (b - 1)
