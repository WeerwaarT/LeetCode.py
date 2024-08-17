# 2530. 执行 K 次操作后的最大分数
# https://leetcode.cn/problems/maximal-score-after-applying-k-operations/
import heapq
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)
        for _ in range(k):
            score -= heapq.heapreplace(nums, nums[0] // 3)

        return score
