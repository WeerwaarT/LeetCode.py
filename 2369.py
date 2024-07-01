from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] and self.validTwo(nums[i - 2], nums[i - 1])
            if i >= 3:
                dp[i] = dp[i] or (dp[i - 3] and self.validThree(nums[i - 3], nums[i - 2], nums[i - 1]))
        return dp[-1]

    def validTwo(self, num1: int, num2: int) -> bool:
        return num1 == num2

    def validThree(self, num1: int, num2: int, num3: int) -> bool:
        return (num1 == num2 == num3) or (num1 + 2 == num2 + 1 == num3)

    # def validPartition(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     f = [True] + [False] * n
    #     for i, x in enumerate(nums):
    #         if i > 0 and f[i - 1] and x == nums[i - 1] or \
    #                 i > 1 and f[i - 2] and (x == nums[i - 1] == nums[i - 2] or
    #                                         x == nums[i - 1] + 1 == nums[i - 2] + 2):
    #             f[i + 1] = True
    #     return f[n]
