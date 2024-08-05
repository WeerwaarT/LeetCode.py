# 8038. 收集元素的最少操作次数
# https://leetcode.cn/contest/biweekly-contest-114/problems/minimum-operations-to-collect-elements/
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        my_set = set()
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] <= k:
                my_set.add(nums[i])
                if len(my_set) == k:
                    return n - i
