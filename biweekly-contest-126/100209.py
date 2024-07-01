from heapq import heappush, heappop
from typing import List


class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        heap = []
        for i, num in enumerate(nums):
            heappush(heap, (num, i))

        marked = [False] * len(nums)
        answer = []
        total = sum(nums)

        for index, k in queries:
            if not marked[index]:
                marked[index] = True
                total -= nums[index]

            while k > 0 and heap:
                num, i = heappop(heap)
                if not marked[i]:
                    marked[i] = True
                    k -= 1
                    total -= num

            answer.append(total)

        return answer
