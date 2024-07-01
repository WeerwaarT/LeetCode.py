from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        cur_max = nums[0]
        left = 0
        sub_arrays = []
        ans = 0
        for i, num in enumerate(nums):
            if num < cur_max:
                continue

            if num == cur_max:
                sub_arrays.append((left + 1, i - 1))
                ans += 1
                continue

            sub_arrays.append((left, i))
            left = i
            cur_max = num

        if sub_arrays[-1][1] != n:
            sub_arrays.append((left, n))

        ans = 0
        for left, right in sub_arrays:
            ans += self.numberOfSubarrays(nums[left:right])

        return ans

