class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = empty_bottles = 0
        while numBottles > 0:
            total += numBottles
            empty_bottles += numBottles
            numBottles = 0
            while empty_bottles >= numExchange:
                empty_bottles -= numExchange
                numBottles += 1
                numExchange += 1

        return total


if __name__ == '__main__':
    print(Solution().maxBottlesDrunk(13, 6))
    print(Solution().maxBottlesDrunk(10, 3))
