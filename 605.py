# 605. 种花问题
# https://leetcode.cn/problems/can-place-flowers/
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        m = len(flowerbed)
        if m == 1:
            return flowerbed[0] == 0

        count = 0
        if (flowerbed[0] + flowerbed[1]) == 0:
            flowerbed[0] = 1
            count += 1

        for i in range(1, m - 1):
            if (flowerbed[i - 1] + flowerbed[i] + flowerbed[i + 1]) == 0:
                flowerbed[i] = 1
                count += 1
                i += 2

        if (flowerbed[-1] + flowerbed[-2]) == 0:
            count += 1

        return count >= n

    # 这个好啊
    # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    #     m = len(flowerbed)
    #     ans = 0
    #     for i in range(m):
    #         if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == m - 1 or flowerbed[i+1] == 0):
    #             ans += 1
    #             flowerbed[i] = 1
    #     return ans >= n

    # 好好好
    # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    #     import math
    #     cur = sum(flowerbed)
    #     lenf = len(flowerbed)
    #     maxf = math.ceil(lenf / 2)
    #     if n > maxf - cur:
    #         return False
    #
    #     flowerbed.insert(0, 0)
    #     flowerbed.insert(-1, 0)
    #
    #     i = 1
    #     while i < (lenf + 1):
    #         if n == 0:
    #             return True
    #
    #         if flowerbed[i] == 0:
    #             if flowerbed[i + 1] == 0:
    #                 n -= 1
    #                 i = i + 2
    #             else:
    #                 i = i + 3
    #         else:
    #             i = i + 2
    #
    #     return n == 0