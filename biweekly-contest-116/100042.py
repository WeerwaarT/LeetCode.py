# 100042. 和为目标值的最长子序列的长度
# https://leetcode.cn/contest/biweekly-contest-116/problems/length-of-the-longest-subsequence-that-sums-to-target/
from collections import defaultdict
from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int, {0: 0})
        for num in nums:
            ndp = dp.copy()
            for k, v in dp.items():
                tmp = k + num
                if tmp <= target:
                    ndp[tmp] = max(ndp[tmp], v + 1)

            dp = ndp

        if target not in dp:
            return -1

        return dp[target]


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubsequence([1, 2, 3, 4, 5, 19], 9))
    print(Solution().lengthOfLongestSubsequence([4, 1, 3, 2, 1, 5], 7))
