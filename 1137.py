# 1137. 第 N 个泰波那契数
# https://leetcode.cn/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        f0, f1, f2 = 0, 1, 1

        while n > 0:
            f0, f1, f2 = f1, f2, f0 + f1 + f2
            n -= 1

        return f0