# 509. 斐波那契数
# https://leetcode.cn/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        f0, f1 = 0, 1

        while n > 0:
            f0, f1 = f1, f0 + f1
            n -= 1

        return f0