import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while len(nums) >= 2:
            num1 = heapq.heappop(nums)
            if num1 >= k:
                break

            num2 = heapq.heappop(nums)
            heapq.heappush(nums, num1 * 2 + num2)
            count += 1

        return count
