# 1654. 到家的最少跳跃次数
# https://leetcode.cn/problems/minimum-jumps-to-reach-home/
from collections import deque
from typing import List


class Solution:
    # fastest
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        q = deque()
        q.append((0, 0, 0))
        seen = {0, }
        upper = max(max(forbidden) + a, x) + b
        while q:
            pos, back, steps = q.popleft()
            if pos == x:
                return steps
            if back == 0:
                n = pos - b
                if n > 0 and n not in forbidden and n not in seen:
                    q.append((n, back + 1, steps + 1))
                    seen.add(n)
            n = pos + a
            if n <= upper and n not in forbidden and n not in seen:
                q.append((n, 0, steps + 1))
                seen.add(n)

        return -1

    # just simply correct
    # def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
    #     q, visited = deque([[0, 1, 0]]), set([0])
    #     lower, upper = 0, max(max(forbidden) + a, x) + b
    #     forbiddenSet = set(forbidden)
    #     while q:
    #         position, direction, step = q.popleft()
    #         if position == x:
    #             return step
    #         nextPosition = position + a
    #         nextDirection = 1
    #         if lower <= nextPosition <= upper and nextPosition * nextDirection not in visited and nextPosition not in forbiddenSet:
    #             visited.add(nextPosition * nextDirection)
    #             q.append([nextPosition, nextDirection, step + 1])
    #         if direction == 1:
    #             nextPosition = position - b
    #             nextDirection = -1
    #             if lower <= nextPosition <= upper and nextPosition * nextDirection not in visited and nextPosition not in forbiddenSet:
    #                 visited.add(nextPosition * nextDirection)
    #                 q.append([nextPosition, nextDirection, step + 1])
    #     return -1

    # my version, totally wrong and I can't find the problem
    # def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
    #     if a in forbidden:
    #         return -1
    #
    #     queue = deque()
    #     queue.append((a, True))
    #     dp = {}
    #     furthest = max(max(forbidden) + a, x) + b
    #     for f in forbidden:
    #         dp[f] = -1
    #
    #     dp[a] = 1
    #     while queue:
    #         cur, can_jump_backward = queue.popleft()
    #         if cur == x:
    #             break
    #
    #         forward = cur + a
    #         if forward <= furthest and dp.get(forward, 0) == 0:
    #             queue.append((forward, True))
    #             dp[forward] = dp[cur] + 1
    #
    #         if can_jump_backward:
    #             backward = cur - b
    #             if (0 <= backward <= furthest) and dp.get(backward, 0) == 0:
    #                 queue.append((backward, False))
    #                 dp[backward] = dp[cur] + 1
    #
    #     return dp.get(x, -1)


print(Solution().minimumJumps([162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98], 29, 98, 80))