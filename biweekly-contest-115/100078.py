# 100078. 最长相邻不相等子序列 I
# https://leetcode.cn/contest/biweekly-contest-115/problems/longest-unequal-adjacent-groups-subsequence-i/
from typing import List


class Solution:
    # def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
    #     if n == 1:
    #         return words
    #
    #     ans = [words[0]]
    #     for i in range(1, n):
    #         if groups[i] != groups[i - 1]:
    #             ans.append(words[i])
    #
    #     return ans

    def getWordsInLongestSubsequence(
        self, n: int, words: List[str], groups: List[int]
    ) -> List[str]:
        f = [1] * n
        g = [-1] * n
        for i in range(n):
            for j in range(i):
                if (
                    f[j] + 1 > f[i]
                    and groups[i] != groups[j]
                ):
                    f[i] = f[j] + 1
                    g[i] = j
        x = f.index(max(f))
        res = []
        while x != -1:
            res.append(x)
            x = g[x]
        return [words[i] for i in reversed(res)]


if __name__ == '__main__':
    print(Solution().getWordsInLongestSubsequence(3, ['e', 'a', 'b'], [0, 0, 1]))
    print(Solution().getWordsInLongestSubsequence(4, ['a', 'b', 'c', 'd'], [1, 0, 1, 1]))