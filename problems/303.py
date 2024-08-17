# from itertools import accumulate
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = []
        sub_sum = 0
        for num in nums:
            sub_sum += num
            self.nums.append(sub_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        else:
            return self.nums[right] - self.nums[left - 1]


#
# class NumArray:
#
#     def __init__(self, nums: List[int]):
#         self.s = list(accumulate(nums, initial=0))
#         # print(self.s)
#
#     def sumRange(self, left: int, right: int) -> int:
#         return self.s[right + 1] - self.s[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)