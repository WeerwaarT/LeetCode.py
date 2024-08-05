# 2698. 求一个整数的惩罚数
# https://leetcode.cn/problems/find-the-punishment-number-of-an-integer/


punishments = [1, 9, 10]


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def f(n1: int, n2: int) -> bool:
            length = len(str(n2))
            n2_str = str(n2)
            if len(str(n1)) >= length:
                return n1 == n2

            for j in range(1, length):
                left = int(n2_str[:j])
                if f(n1 - left, int(n2_str[j:])):
                    return True

            return False

        pn = 0
        for p in punishments:
            if p <= n:
                pn += p ** 2

        for i in range(punishments[-1] + 1, n + 1):
            if f(i, sqr := i ** 2):
                punishments.append(i)
                pn += sqr

        return pn


if __name__ == '__main__':
    print(Solution().punishmentNumber(10) == 182)
    print(Solution().punishmentNumber(37) == 1478)
