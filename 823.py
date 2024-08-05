# 823. 带因子的二叉树
# https://leetcode.cn/problems/binary-trees-with-factors/
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        ans = [1] * len(arr)
        mod = 10 ** 9 + 7
        for i, num in enumerate(arr):
            left, right = 0, i - 1
            while left <= right:
                product = arr[left] * arr[right]
                if product > num:
                    right -= 1
                    continue

                if product < num:
                    left += 1
                    continue

                if left != right:
                    ans[i] += 2 * ans[left] * ans[right]
                else:
                    ans[i] += ans[left] * ans[right]

                ans[i] %= mod
                left += 1
                right -= 1

        return sum(ans) % mod


print(Solution().numFactoredBinaryTrees([2,4,5,10]))
