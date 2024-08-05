# 2240. 买钢笔和铅笔的方案数
# https://leetcode.cn/problems/number-of-ways-to-buy-pens-and-pencils/


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        a = total // cost1
        b = total // cost2
        if b < a:
            a, cost1, cost2 = b, cost2, cost1

        count = 0
        balance = total + cost1
        for i in range(a + 1):
            balance -= cost1
            count += balance // cost2 + 1

        return count

    # 嗯，魔法
    # def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:#类欧几里得算法
    #     def ojld(a,b,c,n):#求sum_{i=0}^{n}floor((a*i+b)/c)
    #         if not (n and a):
    #             return b//c#(n+1)*
    #         if a>=c or b>=c:
    #             return n*(n+1)//2*(a//c)+(n+1)*(b//c)+ojld(a%c,b%c,c,n)#注意(b//c)和(b//c)的括号不能去掉
    #         m=(a*n+b)//c
    #
    #         return m*n-ojld(c,c-b-1,a ,m-1)
    #
    #     return ojld(cost1,total%cost1,cost2,total//cost1)+total//cost1+1
    #     # return ojld(cost1,total,cost2,total//cost1)#-ojld(2*cost1,0,cost2,total//cost1)#要把a转成整数


print(Solution().waysToBuyPensPencils(20, 5, 10))