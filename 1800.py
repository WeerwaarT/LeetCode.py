from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        last = 0
        s_current = 0
        s_max = 0

        for num in nums:
            if num > last:
                s_current += num
            else:
                s_max = max(s_max, s_current)
                s_current = num

            last = num

        return max(s_max, s_current)

    def maxAscendingSum_(self, nums: List[int]) -> int:
        ans = res = nums[0]
        length = len(nums)
        for i in range(1, length):
            if nums[i] > nums[i - 1]:
                res += nums[i]
            else:
                ans = max(ans, res)
                res = nums[i]
        ans = max(ans, res)
        return ans
