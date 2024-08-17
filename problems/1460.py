from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()

        for i in range(len(target)):
            if target[i] != arr[i]:
                return False

        return True

    def _canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)


A = Solution()
print(A.canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]))
