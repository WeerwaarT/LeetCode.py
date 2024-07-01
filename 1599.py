from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 <= runningCost:
            return -1

        n = len(customers)
        max_profit, min_rotation = -1, 0
        cur_profit, cur_rotation = 0, 0
        waiting_customer = 0
        while True:
            if cur_rotation < n:
                waiting_customer += customers[cur_rotation]

            boarding_customer = min(4, waiting_customer)
            waiting_customer -= boarding_customer
            cur_profit += boarding_customer * boardingCost - runningCost
            cur_rotation += 1
            if cur_profit > max_profit:
                min_rotation = cur_rotation
                max_profit = cur_profit

            if cur_rotation >= n and waiting_customer == 0:
                break

        return min_rotation if max_profit > 0 else -1


if __name__ == '__main__':
    print(Solution().minOperationsMaxProfit([8, 3], 5, 6))
