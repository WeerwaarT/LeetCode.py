from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        or_result = 0
        min_length = float('inf')
        while right < len(nums):
            or_result |= nums[right]
            while or_result >= k and left <= right:
                min_length = min(min_length, right - left + 1)
                left += 1
                or_result = 0  # Reset or_result
                for i in range(left, right + 1):  # Recalculate or_result for the new window
                    or_result |= nums[i]
            right += 1

        return min_length if min_length != float('inf') else -1
