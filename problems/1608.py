from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums) + 1):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= i:
                    right = mid
                else:
                    left = mid + 1

            if len(nums) - left == i and nums[left] >= i:
                return i

        return -1

    def specialArray_(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(1, n + 1):
            if nums[i - 1] >= i and (i == n or nums[i] < i):
                return i
        return -1

    def specialArray__(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        for i in range(1, n + 1):
            if nums[i - 1] >= i and (i == n or nums[i] < i):
                return i
        return -1


print(Solution().specialArray([0, 0]))
