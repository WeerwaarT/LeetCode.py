# 740. 删除并获得点数
# https://leetcode.cn/problems/delete-and-earn/
import collections
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += num

        keys = sorted(counter.keys())
        max_points = 0
        vals = [counter[keys[0]]]

        def rob() -> None:
            nonlocal max_points
            m = len(vals)
            if m == 1:
                max_points += vals[0]
                return

            pre, pre_pre = vals[0], 0
            for j in range(1, m):
                cur = max(pre, pre_pre + vals[j])
                pre, pre_pre = cur, pre

            max_points += pre

        n = len(keys)
        for i in range(1, n):
            if keys[i] == keys[i - 1] + 1:
                vals.append(counter[keys[i]])
            else:
                rob()
                vals = [counter[keys[i]]]

        rob()
        return max_points


if __name__ == '__main__':
    print(Solution().deleteAndEarn([1, 2, 3]))
    print(Solution().deleteAndEarn([3,4,2]))
    print(Solution().deleteAndEarn([2,2,3,3,3,4]))
    print(Solution().deleteAndEarn([1,1,1,2,4,5,5,5,6]))
