from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        s = sum(arr)

        if s % 3:
            return [-1, -1]

        if s == 0:
            return [0, 2]

        one_third = s // 3
        i = 0

        while True:             # 跳过前三分之一个1的前导0
            if arr[i]:
                break

            i += 1

        a = i
        count = 0

        while count < one_third:    # 前三分之一个1
            if arr[i]:
                count += 1

            i += 1

        while True:             # 前三分之一个1与中三分之一个1之间的0
            if arr[i]:
                break

            i += 1
