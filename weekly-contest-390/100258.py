import collections
import heapq
from typing import List


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        heap = []
        life = {}
        track = collections.defaultdict(int)
        n = len(nums)
        ans = []
        for i in range(n):
            num, fre = nums[i], freq[i]
            track[num] += fre
            life[num] = i
            heapq.heappush(heap, (-track[num], num, i))
            while True:
                cur_max, cur_num, cur_life = heapq.heappop(heap)
                if cur_life == life[cur_num]:
                    ans.append(-cur_max)
                    heapq.heappush(heap, (cur_max, cur_num, cur_life))
                    break

        return ans
