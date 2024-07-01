import collections
import math


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def dfs(freq, deletions):
            if not freq:
                return deletions

            min_freq, max_freq = freq[0], freq[-1]
            if max_freq - min_freq <= k:
                return deletions

            delete_min_option = dfs(freq[1:], deletions + min_freq)
            delete_max_option = dfs(freq[:-1], deletions + max_freq - min_freq - k)
            return min(delete_min_option, delete_max_option)

        return dfs(sorted(collections.Counter(word).values()), 0)

    # def minimumDeletions(self, word: str, k: int) -> int:
    #     nums = collections.Counter(word).values()
    #
    #     def calc(v):
    #         res = 0
    #         for x in nums:
    #             if x < v:
    #                 res += x
    #             elif x > v + k:
    #                 res += x - v - k
    #         return res
    #
    #     return min(calc(i) for i in range(len(word) + 1))
    #
    # def minimumDeletions(self, word: str, k: int) -> int:
    #     nums = collections.Counter(word).values()
    #
    #     def calc(v):
    #         res = 0
    #         for x in nums:
    #             if x < v:
    #                 res += x
    #             elif x > v + k:
    #                 res += x - v - k
    #         return res
    #
    #     ans = math.inf
    #     for x in nums:
    #         for v in [max(0, x - k), x]:
    #             ans = min(ans, calc(v))
    #     return ans
