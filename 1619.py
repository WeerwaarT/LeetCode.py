from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        return sum(arr[int(len(arr) * 0.05):len(arr) - int(len(arr) * 0.05)]) / (len(arr) * 0.9)

    def trimMean_(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        return sum(arr[n // 20: -n // 20]) / (n * 0.9)

    def trimMean__(self, arr: List[int]) -> float:
        return sum(sorted(arr)[len(arr) // 20:len(arr) - len(arr) // 20]) / (len(arr) - 2 * (len(arr) // 20))
