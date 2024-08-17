# 2652. 倍数求和
# https://leetcode.cn/problems/sum-multiples/


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total = 0
        for i in range(3, n + 1):
            if i % 3 == 0:
                total += i
            elif i % 5 == 0:
                total += i
            elif i % 7 == 0:
                total += i

        return total

    # 很帅
    # def sumOfMultiples(self, n: int) -> int:
    #     def s(m:int)->int:
    #         return n//m*(n//m+1)//2*m
    #     return s(3)+s(5)+s(7)-s(15)-s(21)-s(35)+s(105)
