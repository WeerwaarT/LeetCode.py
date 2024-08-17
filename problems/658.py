from bisect import bisect_left
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1

        while left < right - 1:
            mid = (left + right) // 2
            if arr[mid] > x:
                right = mid
            else:
                left = mid

        left = right - 1
        output = []

        while k:
            if left < 0:
                for _ in range(k):
                    output.append(arr[right])
                    right += 1

                break

            if right == len(arr):
                for _ in range(k):
                    output.append(arr[left])
                    left -= 1

                break

            if abs(arr[right] - x) < abs(arr[left] - x):
                output.append(arr[right])
                right += 1
                k -= 1
            else:
                output.append(arr[left])
                left -= 1
                k -= 1

        return sorted(output)

    def findClosestElements_(self, arr, k, x):
        left = 0
        right = len(arr) - k
        while left < right:
            mid = (right + left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left: left + k]

    def findClosestElements__(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda v: abs(v - x))
        return sorted(arr[:k])

    def findClosestElements___(self, arr: List[int], k: int, x: int) -> List[int]:
        right = bisect_left(arr, x)
        left = right - 1
        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= len(arr) or x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left + 1: right]


print(Solution().findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5))
