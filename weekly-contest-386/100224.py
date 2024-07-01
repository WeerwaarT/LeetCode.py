import collections
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 1:
            return False

        counter = collections.Counter(nums)
        most_common = counter.most_common(1)
        if most_common[0][1] <= 2:
            return True
        else:
            return False
