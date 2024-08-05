# 8014. 循环增长使字符串子序列等于另一个字符串
# https://leetcode.cn/contest/biweekly-contest-111/problems/make-string-a-subsequence-using-cyclic-increments/

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n1, n2 = len(str1), len(str2)
        if n1 < n2:
            return False

        left = right = 0
        c = ord('a')

        while left < n1 and right < n2:
            a = ord(str1[left])
            b = ord(str2[right])
            if b == a or b == ((a - c + 1) % 26 + c):
                left += 1
                right += 1
            else:
                left += 1

        if right == n2:
            return True

        return False
