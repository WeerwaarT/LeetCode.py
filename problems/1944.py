from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [1] * n
        ans[-1] = 0
        
