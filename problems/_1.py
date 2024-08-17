from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = defaultdict(list)
        for i, g in enumerate(nums):
            x.