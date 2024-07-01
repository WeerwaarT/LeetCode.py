import math
from typing import List
from sortedcontainers import SortedDict


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        amounts = SortedDict()
        for coin in coins:
            amounts[coin] = [coin]

        count = 0
        while count < k:
            amount, coins = amounts.popitem(0)
            count += 1
            for coin in coins:
                new_amount = amount + coin
                if new_amount in amounts:
                    amounts[new_amount].append(coin)
                else:
                    amounts[new_amount] = [coin]

        return next(iter(amounts.items()))[0]

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def lcm(x: int, y: int) -> int:
            return abs(x * y) // math.gcd(x, y)

        new_coins = []
        n = len(coins)
        for i in range(n):
            new_coins.append(coins[i])
            for j in range(i + 1, n):
                new_coins.append(lcm(coins[i], coins[j]))

        new_coins.sort()
        new_n = len(new_coins)
        return new_coins[k % new_n] * (k // new_n)
