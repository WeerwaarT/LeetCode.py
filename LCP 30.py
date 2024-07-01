import heapq
from collections import deque
from typing import List


class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0:
            return -1

        hp = 1
        queue = deque(nums)
        heap = []
        count = 0
        while len(queue):
            room = queue.popleft()
            if room < 0:
                heapq.heappush(heap, room)

            hp += room
            while hp <= 0:
                adjust = heapq.heappop(heap)
                hp -= adjust
                queue.append(adjust)
                count += 1

        return count if hp > 0 else -1

    # def magicTower(self, nums: List[int]) -> int:
    #     if sum(nums) < 0:
    #         return -1
    #     ans = 0
    #     hp = 1
    #     h = []
    #     for x in nums:
    #         if x < 0:
    #             heappush(h, x)
    #         hp += x
    #         if hp < 1:
    #             # 这意味着 x < 0，所以前面必然会把 x 入堆
    #             # 所以堆必然不是空的，并且堆顶 <= x
    #             hp -= heappop(h)  # 反悔
    #             ans += 1
    #     return ans
