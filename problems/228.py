# 228. 汇总区间
# https://leetcode.cn/problems/summary-ranges/
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if not n:
            return []

        ranges = []
        i = 0
        left = right = nums[i]
        while i < n - 1:
            i += 1
            if (next_right := nums[i]) - right != 1:
                if left != right:
                    ranges.append(f'{left}->{right}')
                else:
                    ranges.append(f'{left}')

                left = right = next_right
            else:
                right = next_right

        if left != right:
            ranges.append(f'{left}->{right}')
        else:
            ranges.append(f'{left}')

        return ranges


print(Solution().summaryRanges([0,1,2,4,5,7]))