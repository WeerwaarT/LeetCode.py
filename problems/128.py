from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums_set:    # Using nums_set significantly optimize cases with massive duplicate elements
            if num - 1 not in nums_set:
                cur_length = 0
                while num in nums_set:
                    cur_length += 1
                    num += 1

                longest = max(longest, cur_length)

        return longest
