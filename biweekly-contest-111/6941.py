# 6941. 将三个组排序
# https://leetcode.cn/contest/biweekly-contest-111/problems/sorting-three-groups/
from collections import defaultdict
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        table = defaultdict(list)
        for i, num in enumerate(nums):
            table[num].append(i)

        def a(b: list) -> int:
            count = 0
            left, right = 0, 1
            while right < n:
                if b[left] < b[right]:
                    left += 1
                    right += 1
                else:
                    count += 1
                    right += 1

            return count
        return min(a(table[1] + table[2] + table[3]), a(table[3] + table[2] + table[1]))

# class Solution:
#     def minimumOperations(self, nums: List[int]) -> int:
#         dp1, dp2, dp3 = 0, 0, 0
#         for num in nums:
#             # 这里的 1, 2, 3 实际上指的是下一位可以填的最小数字
#             # dp1：下一位是 1，因此只能前面都是 1，只能从 dp1 来，因此如果数 > 1 需要使用 dp1 + 1
#             # dp2: 下一位是 2，前面可以是 1 / 2，如果从 1 转移，即前面要求当前位置不小于 1，则只需要把 num 调整到 <= 2 即可；如果前面要求当前位置不小于 2，则这个位置只能是 2
#             # dp3：逻辑与 dp2 类似
#             dp1, dp2, dp3 = dp1 + (num > 1), min(dp1, dp2 + (num < 2)) + (num > 2), min(dp1, dp2 + (num < 2), dp3 + (num < 3))
#         return dp3

print(Solution().minimumOperations([3,3,2]))