# 2591. 将钱分给最多的儿童
# https://leetcode.cn/problems/distribute-money-to-maximum-children/


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children > money:
            return -1

        money -= children
        n = money // 7
        if n > children:
            return children - 1
        elif n == children:
            return children if money % 7 == 0 else children - 1
        elif n == 0:
            return 0
        else:
            return n if (money - 7 * n) != 3 or (children - n) != 1 else n - 1


print(Solution().distMoney(20, 3))
