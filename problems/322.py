from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}
        for coin in coins:
            if coin > amount:
                coins.remove(coin)
            else:
                dp[coin] = 1

        m = min(coins)
        for i in range(m, amount - m + 1):
            if i not in dp:
                continue

            for coin in coins:
                next_amount = i + coin
                if next_amount > amount:
                    continue

                if next_amount in dp:
                    dp[next_amount] = min(dp[next_amount], dp[i] + 1)
                else:
                    dp[next_amount] = dp[i] + 1

        return dp[amount] if amount in dp else -1


if __name__ == '__main__':
    print(Solution().coinChange([1, 2, 5], 11))
    print(Solution().coinChange([2], 3))
    print(Solution().coinChange([1], 0))
    print(Solution().coinChange([2147483647], 2))
