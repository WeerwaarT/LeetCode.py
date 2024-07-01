import collections
from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        my_set1 = set()
        my_set2 = set()
        for num in arr1:
            s = str(num)
            for i in range(1, len(s) + 1):
                my_set1.add(s[:i])

        for num in arr2:
            s = str(num)
            for i in range(1, len(s) + 1):
                my_set2.add(s[:i])

        longest = 0
        my_set3 = my_set1.intersection(my_set2)
        for i in my_set3:
            longest = max(longest, len(i))

        return longest
