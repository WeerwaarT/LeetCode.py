from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        left, right = 0, 1
        ans = 1
        while right < n:
            if nums[right] <= nums[right - 1]:
                left = right

            ans = max(ans, right - left + 1)
            right += 1

        left, right = 0, 1
        while right < n:
            if nums[right] >= nums[right - 1]:
                left = right

            ans = max(ans, right - left + 1)
            right += 1

        return ans
