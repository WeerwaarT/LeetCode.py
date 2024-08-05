# 1333. 餐厅过滤器
# https://leetcode.cn/problems/filter-restaurants-by-vegan-friendly-price-and-distance/
import heapq
from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        filtered = []
        for i, r, v, p, d in restaurants:
            if v < veganFriendly:
                continue

            if p <= maxPrice and d <= maxDistance:
                heapq.heappush(filtered, (r, i))

        ans = [heapq.heappop(filtered)[1] for _ in range(len(filtered))]
        ans.reverse()
        return ans

    def filterRestaurants(self, restaurants: list[list[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> list[int]:
        ans = []
        for cur in restaurants:
            if cur[2] >= veganFriendly and cur[3] <= maxPrice and cur[4] <= maxDistance:
                ans.append(cur)
        ls = sorted(ans, key=lambda x : (x[1], x[0]), reverse = True)   # filtered.sort(key=lambda r: (-r[1], -r[0]))
        res = []
        for i in ls:
            res.append(i[0])
        return res