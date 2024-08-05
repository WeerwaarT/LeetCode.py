# 6954. 统计和小于目标的下标对数目
# https://leetcode.cn/contest/biweekly-contest-111/problems/count-pairs-whose-sum-is-less-than-target/
from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        table = defaultdict(list)

        for i, n in enumerate(nums):
            table[n].append(i)

        for i, n in enumerate(nums):
            minus = target - n
            count += sum(1 for key, indices in table.items() if key < minus for index in indices if index > i)

        return count
