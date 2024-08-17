# 833. 字符串中的查找与替换
# https://leetcode.cn/problems/find-and-replace-in-string/
from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        k = len(indices)
        replaced = [c for c in s]
        print(replaced)

        for i in range(k):
            left = indices[i]
            right = left + len(sources[i])
            substr = s[left:right]
            if substr == sources[i]:
                for j in range(left, right):
                    replaced[j] = ''

                replaced[left] = targets[i]

        ans = ""
        for c in replaced:
            ans += c[0]

        return "".join(replaced)