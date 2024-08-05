# 275. H 指数 II
# https://leetcode.cn/problems/h-index-ii/
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if sum(citations) == 0:
            return 0

        h = 0
        n = len(citations)
        for i in range(n - 1, -1, -1):
            if citations[i] > h:
                h += 1
            else:
                break

        return h

    # 懒得写二分，抄了
    # def hIndex(self, citations: List[int]) -> int:
    #     a, b = 0, len(citations) - 1
    #     if citations[a] >= len(citations):
    #         return len(citations)
    #     if citations[b] <= 1:
    #         return citations[b]
    #     while b > a + 1:
    #         c = (b + a) // 2
    #         if citations[c] >= (len(citations) - c):
    #             b = c
    #         else:
    #             a = c
    #     # if citations[b] >= len(citations) - b:
    #     return len(citations) - b
