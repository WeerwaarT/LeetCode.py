# 1726. 同积元组
# https://leetcode.cn/problems/tuple-with-same-product/
import collections
from itertools import combinations
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = collections.defaultdict(int)
        n = len(nums)
        for i in range(n):
            a = nums[i]
            for j in range(i + 1, n):
                b = nums[j]
                products[a * b] += 1

        count = 0
        for v in products.values():
            count += v * (v - 1) * 4

        return count

    # 逻辑是一样的速度却快了一些
    # def tupleSameProduct(self, nums: List[int]) -> int:
    #     return 4 * sum(c * (c - 1) for c in collections.Counter(a * b for a, b in combinations(nums, 2)).values())


if __name__ == '__main__':
    print(Solution().tupleSameProduct([2, 3, 4, 6]))
    print(Solution().tupleSameProduct([1, 2, 4, 5, 10]))
