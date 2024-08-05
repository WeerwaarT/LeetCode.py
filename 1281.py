# 1281. 整数的各位积和之差
# https://leetcode.cn/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        he = 0
        ji = 1

        while n > 0:
            a = n % 10
            he += a
            ji *= a
            n //= 10

        return ji - he

    # 好蠢啊，为什么不停的转换类型反而更快
    # def subtractProductAndSum(self, n: int) -> int:
    #     s = str(n)
    #     a = 1
    #     b = 0
    #     for i in range(len(s)):
    #         a = a * int(s[i])
    #         b = b + int(s[i])
    #     return a - b