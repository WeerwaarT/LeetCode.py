# 2682. 找出转圈游戏输家
# https://leetcode.cn/problems/find-the-losers-of-the-circular-game/
from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        received = set()
        i = 0
        while True:
            cur = ((i + pow(i, 2)) * k // 2) % n + 1
            if cur in received:
                break

            received.add(cur)
            i += 1

        return sorted(list(set(range(2, n + 1)) - received))

    # def circularGameLosers(self, n: int, k: int) -> List[int]:
    #     vis = [False] * n
    #     i, d = 0, k
    #     while not vis[i]:
    #         vis[i] = True
    #         i = (i + d) % n
    #         d += k
    #     return [i for i, b in enumerate(vis, 1) if not b]