from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = defaultdict(list)
        for i, num in enumerate(nums):
            my_dict[num].append(i)

        for k, v in my_dict.items():
            if target - k in my_dict:
                if k == target - k:
                    if len(my_dict[k]) > 1:
                        return [my_dict[k][0], my_dict[k][1]]
                    continue

                return [my_dict[k][0], my_dict[target - k][0]]

    def twoSum_(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num not in hashmap:
                hashmap[num] = i
            else:
                return [hashmap[target - num], i]


print(Solution().twoSum([3, 2, 4], 6))
