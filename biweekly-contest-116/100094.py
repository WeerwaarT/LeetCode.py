# 100094. 子数组不同元素数目的平方和 I
# https://leetcode.cn/contest/biweekly-contest-116/problems/subarrays-distinct-element-sum-of-squares-i/
from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        sqr_sum = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                sqr_sum += pow(len(set(nums[i:j])), 2)

        return sqr_sum % mod


if __name__ == '__main__':
    print(Solution().sumCounts([1, 2, 1]) == 15)
    print(Solution().sumCounts([2, 2]) == 3)
