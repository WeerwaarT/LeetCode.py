# from collections import Counter
from typing import List

from sortedcontainers import SortedList as SL


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        sl1 = SL(arr1)
        sl2 = SL(arr2)
        for x in nums[2:]:
            gt1 = len(sl1) - sl1.bisect_right(x)
            gt2 = len(sl2) - sl2.bisect_right(x)
            if gt1 > gt2:
                arr1.append(x)
                sl1.add(x)
            elif gt1 < gt2:
                arr2.append(x)
                sl2.add(x)
            elif len(arr1) <= len(arr2):
                arr1.append(x)
                sl1.add(x)
            else:
                arr2.append(x)
                sl2.add(x)
        return arr1 + arr2

    # 超时
    # def resultArray(self, nums: List[int]) -> List[int]:
    #     def greaterCount(counter: Counter, val: int) -> int:
    #         return sum(count for num, count in counter.items() if num > val)
    #
    #     n = len(nums)
    #     arr1 = [nums[0]]
    #     arr2 = [nums[1]]
    #     counter1 = Counter(arr1)
    #     counter2 = Counter(arr2)
    #     for i in range(2, n):
    #         count1 = greaterCount(counter1, nums[i])
    #         count2 = greaterCount(counter2, nums[i])
    #
    #         if count1 > count2 or (count1 == count2 and len(arr1) <= len(arr2)):
    #             arr1.append(nums[i])
    #             counter1[nums[i]] += 1
    #         else:
    #             arr2.append(nums[i])
    #             counter2[nums[i]] += 1
    #
    #     return arr1 + arr2
