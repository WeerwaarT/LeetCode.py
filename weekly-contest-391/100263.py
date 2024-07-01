class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s, y = 0, x
        while y > 0:
            s += y % 10
            y //= 10

        return s if x % s == 0 else -1
    