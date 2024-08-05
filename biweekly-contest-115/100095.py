# 100095. 上一个遍历的整数
# https://leetcode.cn/contest/biweekly-contest-115/problems/last-visited-integers/
import collections
from typing import List


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        count = 0
        nums = collections.deque()
        ans = []
        for word in words:
            if word != 'prev':
                count = 0
                nums.appendleft(int(word))
            else:
                if len(nums) > count:
                    ans.append(nums[count])
                else:
                    ans.append(-1)

                count += 1

        return ans


if __name__ == '__main__':
    print(Solution().lastVisitedIntegers(["1", "2", "prev", "prev", "prev"]) == [2, 1, -1])
    print(Solution().lastVisitedIntegers(["1", "prev", "2", "prev", "prev"]) == [1, 2, 1])
    print(Solution().lastVisitedIntegers(["1"]) == [])
    print(Solution().lastVisitedIntegers(["1", "prev", "2", "prev", "prev"]) == [1, 2, 1])