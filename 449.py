# 2605. 从两个数字数组里生成最小数字
# https://leetcode.cn/problems/form-smallest-number-from-two-digit-arrays/
from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        if s := set(nums1) & set(nums2):
            return min(s)

        one, two = min(nums1), min(nums2)
        if one < two:
            return 10 * one + two
        else:
            return 10 * two + one
