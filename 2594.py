# 2594. 修车的最少时间
# https://leetcode.cn/problems/minimum-time-to-repair-cars/
from collections import Counter
from math import isqrt
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # 作者：灵茶山艾府
        # 链接：https://leetcode.cn/problems/minimum-time-to-repair-cars/solutions/2177199/er-fen-da-an-pythonjavacgo-by-endlessche-keqf/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        cnt = Counter(ranks)
        left = 0
        right = min(cnt) * cars * cars
        while left + 1 < right:
            mid = (left + right) // 2
            if sum(isqrt(mid // r) * c for r, c in cnt.items()) >= cars:
                right = mid
            else:
                left = mid
        return right


print(Solution().repairCars([3,3,1,2,1,1,3,2,1], 58))