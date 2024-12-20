from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums) - 1
        if n < 2:
            return n

        steps = 0
        cur = 0
        while cur < n:
            if cur + nums[cur] >= n:
                steps += 1
                break

            furthest = 0
            nex = 0
            for i in range(1, nums[cur] + 1):
                if (temp := i + nums[cur + i]) >= furthest:
                    nex = i
                    furthest = temp

            cur = cur + nex
            steps += 1

        return steps
