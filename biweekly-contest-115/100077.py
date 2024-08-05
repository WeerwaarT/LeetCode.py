# 100077. 最长相邻不相等子序列 II
# https://leetcode.cn/contest/biweekly-contest-115/problems/longest-unequal-adjacent-groups-subsequence-ii/
import collections
from typing import List


class Solution:
    # def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
    #     if n == 1:
    #         return words
    #
    #     regrouped_words = collections.defaultdict(list)
    #     for i in range(n):
    #         regrouped_words[len(words[i])].append((words[i], groups[i]))
    #
    #     def is_one_char_diff(str1: str, str2: str) -> bool:
    #         # 如果两个字符串的长度不同，直接返回False
    #         if len(str1) != len(str2):
    #             return False
    #
    #         diff_count = 0  # 初始化不同字符计数器
    #         for ch1, ch2 in zip(str1, str2):
    #             if ch1 != ch2:
    #                 diff_count += 1
    #                 # 如果不同字符数量大于1，提前结束循环并返回False
    #                 if diff_count > 1:
    #                     return False
    #
    #         return diff_count == 1  # 如果正好一个字符不同，返回True
    #
    #     max_len = 0
    #     ans = []
    #     for _, ws in regrouped_words.items():
    #         if len(ws) == 1:
    #             if max_len < 1:
    #                 ans = ws[0][0]
    #                 max_len = 1
    #
    #             continue
    #
    #         temp_ans = [ws[0][0]]
    #         m = len(ws)
    #         i = 1
    #         while i < m:
    #             if is_one_char_diff(ws[i - 1][0], ws[i][0]) and ws[i-1][1] != ws[i][1]:
    #                 temp_ans.append(ws[i][0])
    #             else:
    #                 if len(temp_ans) > max_len:
    #                     max_len = len(temp_ans)
    #                     ans = temp_ans
    #
    #                 temp_ans = [ws[i][0]]
    #
    #             i += 1
    #
    #         if len(temp_ans) > max_len:
    #             max_len = len(temp_ans)
    #             ans = temp_ans
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
                    and len(words[i]) == len(words[j])
                ):
                    ham = 0
                    for k in range(len(words[i])):
                        ham += words[i][k] != words[j][k]
                    if ham == 1:
                        f[i] = f[j] + 1
                        g[i] = j
        x = f.index(max(f))
        res = []
        while x != -1:
            res.append(x)
            x = g[x]
        return [words[i] for i in reversed(res)]


if __name__ == '__main__':
    print(Solution().getWordsInLongestSubsequence(3, ["bab","dab","cab"], [1,2,2]))
    print(Solution().getWordsInLongestSubsequence(3, ["bb", "dab", "cab"], [1, 2, 2]))
    print(Solution().getWordsInLongestSubsequence(3, ["bdb","aaa","ada"], [2,1,3]))