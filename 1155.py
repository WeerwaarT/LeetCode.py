# 1155. 掷骰子等于目标和的方法数
# https://leetcode.cn/problems/number-of-dice-rolls-with-target-sum/


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}

        def f(dice: int, face: int, t: int) -> int:
            if not (dice <= t <= dice * face):
                return 0

            if dice == 1:
                return 1 if t <= face else 0

            if (dice, t) in dp:
                return dp[(dice, t)]

            count = 0
            for i in range(1, face + 1):
                count += f(dice - 1, face, t - i)

            dp[(dice, t)] = count % (10 ** 9 + 7)
            return count % (10 ** 9 + 7)

        # print(f(n, k, target))
        return f(n, k, target)

    # def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    #     if not (n <= target <= n * k):
    #         return 0  # 无法组成 target
    #     mod = 10 ** 9 + 7
    #     f = [1] + [0] * (target - n)
    #     for i in range(1, n + 1):
    #         max_j = min(i * (k - 1), target - n)  # i 个骰子至多掷出 i*(k-1)
    #         for j in range(1, max_j + 1):
    #             f[j] += f[j - 1]  # 原地计算 f 的前缀和
    #         for j in range(max_j, k - 1, -1):
    #             f[j] = (f[j] - f[j - k]) % mod  # f[j] 是两个前缀和的差
    #     return f[-1]


if __name__ == '__main__':
    print(Solution().numRollsToTarget(1, 6, 3) == 1)
    print(Solution().numRollsToTarget(1, 6, 3) == 1)
    print(Solution().numRollsToTarget(3, 6, 10) == 27)
    print(Solution().numRollsToTarget(2, 6, 7) == 6)
    print(Solution().numRollsToTarget(30, 30, 500) == 222616187)
