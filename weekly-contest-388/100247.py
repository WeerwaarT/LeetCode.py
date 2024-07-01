import heapq
from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        total = 0
        offset = 0
        happiness.sort(reverse=True)
        for i in range(k):
            total += max(happiness[i] - offset, 0)
            offset += 1

        return total
