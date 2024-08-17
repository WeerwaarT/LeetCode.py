# 274. H 指数
# https://leetcode.cn/problems/h-index/
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if sum(citations) == 0:
            return 0

        citations.sort(reverse=True)
        h = 0
        n = len(citations)
        while h < n:
            if citations[h] > h:
                h += 1
            else:
                break

        return h


if __name__ == '__main__':
    print(Solution().hIndex([3, 0, 6, 1, 5]))
    print(Solution().hIndex([1, 3, 1]))
    print(Solution().hIndex([1]))
