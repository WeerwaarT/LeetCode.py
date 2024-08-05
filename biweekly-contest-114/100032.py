# 100032. 使数组为空的最少操作次数
# https://leetcode.cn/contest/biweekly-contest-114/problems/minimum-number-of-operations-to-make-array-empty/
import collections
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        my_dict = collections.defaultdict(int)
        for num in nums:
            my_dict[num] += 1

        count = 0
        for k, v in my_dict.items():
            pass


# 来不及做了，算了，这次忘参加了下次再说