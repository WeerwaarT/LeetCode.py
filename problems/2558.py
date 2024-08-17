# 2558. 从数量最多的堆取走礼物
# https://leetcode.cn/problems/take-gifts-from-the-richest-pile/
import heapq
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n = len(gifts)
        for i in range(n):
            gifts[i] = -gifts[i]

        heapq.heapify(gifts)
        for _ in range(k):
            heapq.heapreplace(gifts, -int((-gifts[0]) ** 0.5))

        return -sum(gifts)


if __name__ == '__main__':
    print(Solution().pickGifts([25, 64, 9, 4, 100], 4) == 29)
