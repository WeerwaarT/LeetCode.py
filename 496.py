from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_dict = {}
        stack = [-1]

        for num in reversed(nums2):

            while len(stack) > 1 and num > stack[-1]:
                stack.pop()

            my_dict[num] = stack[-1]
            stack.append(num)

        return [my_dict[num] for num in nums1]


print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
