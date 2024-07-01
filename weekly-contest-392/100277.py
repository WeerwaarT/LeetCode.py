import heapq
from typing import List


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        max_heap = [-num for num in nums[:n // 2]]
        min_heap = nums[n // 2:]
        heapq.heapify(max_heap)
        heapq.heapify(min_heap)
        operations = 0
        while min_heap[0] != k:
            # 三种情况
            # k在min_heap[0]和-max_heap[0]之间
            # 或者k小于那两者
            # 或者k大于那两者
            pass

        return operations
