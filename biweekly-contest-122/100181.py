from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_0 = nums[0]
        nums = nums[1:]
        min_1 = min(nums)
        nums.remove(min_1)
        min_2 = min(nums)
        return min_0 + min_1 + min_2


if __name__ == '__main__':
    print(Solution().minimumCost([1, 2, 3, 12]))
    print(Solution().minimumCost([5, 4, 3]))
    print(Solution().minimumCost([10, 3, 1, 1]))
