# 2578. 最小和分割
# https://leetcode.cn/problems/split-with-minimum-sum/
import collections


class Solution:
    def splitNum(self, num: int) -> int:
        digits = []
        while num:
            digits.append(num % 10)
            num //= 10

        digits.sort()
        n = len(digits)
        num1, num2 = 0, 0
        for i in range(1, n, 2):
            num1 = num1 * 10 + digits[i - 1]
            num2 = num2 * 10 + digits[i]

        if n % 2 == 1:
            num1 = num1 * 10 + digits[-1]

        return num1 + num2