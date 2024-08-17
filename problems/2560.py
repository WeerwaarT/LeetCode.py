# 2560. House Robber IV
# https://leetcode.cn/problems/house-robber-iv/
from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        my_set = set(nums)
        my_key = sorted(my_set)
        left = 0
        right = len(my_key)-1
        while left <= right:
            mid = (left + right)//2
            ability = my_key[mid]
            flag = 0
            num_of_house = 0
            for i in nums:
                if flag == 0:
                    if i <= ability:
                        num_of_house += 1
                        flag = 1
                else:
                    flag = 0
            if num_of_house >= k:
                right = mid - 1
            else:
                left = mid + 1
        return my_key[left]


print(Solution().minCapability([2,7,9,3,1], 2))