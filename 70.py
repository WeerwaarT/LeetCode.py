# 70. 爬楼梯
# https://leetcode.cn/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        f0, f1 = 1, 2

        for i in range(2, n):
            f0, f1 = f1, f0 + f1

        return f1