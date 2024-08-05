from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cumulative_sum = 0
        start_value = 1

        for i in nums:
            cumulative_sum += i
            start_value = max(start_value, 1 - cumulative_sum)

        return start_value
