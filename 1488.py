# 1488. 避免洪水泛滥
# https://leetcode.cn/problems/avoid-flood-in-the-city/
import collections
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        hasRained = {}
        allRains = []
        dryDates = collections.deque()
        for i, rain in enumerate(rains):
            if rain:
                allRains.append((i, rain))
            else:
                dryDates.append(i)

        ans = [1] * len(rains)
        for i, rain in allRains:
            ans[i] = -1
            if rain not in hasRained:
                hasRained[rain] = i
            else:
                cache = []
                dried = False
                # 用二分查找理应更快一些，然而并没有
                while len(dryDates):
                    dry = dryDates.popleft()
                    if dry < hasRained[rain]:
                        cache.append(dry)
                        continue

                    if dry > i:
                        return []

                    dried = True
                    ans[dry] = rain
                    hasRained[rain] = i
                    break

                if not dried:
                    return []

                while cache:
                    dryDates.appendleft(cache.pop())

        return ans

    # def avoidFlood(self, rains: List[int]) -> List[int]:
    #     fullLakes = {}
    #     allRainingDays = []
    #     dryDates = []
    #     for i, rain in enumerate(rains):
    #         if rain:
    #             allRainingDays.append((i, rain))
    #         else:
    #             dryDates.append(i)
    #
    #     ans = [1] * len(rains)
    #     for i, rain in allRainingDays:
    #         ans[i] = -1
    #         if rain not in fullLakes:
    #             fullLakes[rain] = i
    #         else:
    #             left, mid, right = 0, 0, len(dryDates) - 1
    #             dry = -1
    #             while left <= right:
    #                 mid = left + (right - left) // 2
    #                 if dryDates[mid] > fullLakes[rain]:
    #                     dry = dryDates[mid]
    #                     right = mid - 1
    #                 else:
    #                     left = mid + 1
    #
    #             if dry < 0 or dry > i:
    #                 return []
    #             else:
    #                 dryDates.pop(left)
    #                 ans[dry] = rain
    #                 fullLakes[rain] = i
    #
    #     return ans


if __name__ == '__main__':
    print(Solution().avoidFlood([1, 1, 0, 0]))
    print(Solution().avoidFlood([0, 1, 1]))
    print(Solution().avoidFlood([1, 2, 3, 4]))
    print(Solution().avoidFlood([1, 2, 0, 0, 2, 1]))
    print(Solution().avoidFlood([1, 2, 0, 1, 2]))
    print(Solution().avoidFlood([1, 2, 0, 2, 3, 0, 1]))
    print(Solution().avoidFlood([1, 0, 2, 0, 2, 1]))
    print(Solution().avoidFlood([1, 0, 2, 0, 3, 0, 2, 0, 0, 0, 1, 2, 3]))