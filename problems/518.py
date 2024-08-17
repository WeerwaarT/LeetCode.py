import collections
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = collections.defaultdict(int)
        for c in coins:
            dp[c] = 1

        for a in range(1, amount):
            if dp[a] == 0:
                continue

            for c in coins:
                dp[a + c] += dp[a]

        return dp[amount] // 2


if __name__ == '__main__':
    print(Solution().change(3, [2]))
    print(Solution().change(5, [1, 2, 5]))
