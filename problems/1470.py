from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if n == 1:
            return nums

        shuffled = []

        for i in range(n):
            shuffled.append(nums[i])
            shuffled.append(nums[i + n])

        return shuffled

    def _shuffle(self, nums: List[int], n: int) -> List[int]:
        nums[::2], nums[1::2] = nums[:n], nums[n:]
        return nums
