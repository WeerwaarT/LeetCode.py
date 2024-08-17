from typing import List


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        i = len(nums) - 2

        while i >= 0:
            if i == len(nums) - 1:
                i -= 1
                continue

            if nums[i] <= nums[i + 1]:
                nums[i] = nums[i] + nums[i + 1]
                nums.pop(i + 1)
            else:
                i -= 1

        return max(nums)

    # def maxArrayValue(self, nums: List[int]) -> int:
    #     ans = 0
    #     for x in reversed(nums):
    #         if x > ans:
    #             ans = x
    #         else:
    #             ans += x
    #     return ans


if __name__ == '__main__':
    print(Solution().maxArrayValue([2, 3, 7, 9, 3]))
    print(Solution().maxArrayValue(([5, 3, 3])))
