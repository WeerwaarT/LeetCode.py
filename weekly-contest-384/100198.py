import re
from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        s = ''
        for i in range(n - 1):
            if (diff := nums[i + 1] - nums[i]) > 0:
                s += '1'
            elif diff == 0:
                s += '0'
            else:
                s += '-'

        p = ''
        for i in range(m):
            if pattern[i] == -1:
                p += '-'
            else:
                p += str(pattern[i])

        print(s)
        print(p)
        count = 0
        for i in range(n - m):
            count += 1 if s[i:i + m] == p else 0

        return count
