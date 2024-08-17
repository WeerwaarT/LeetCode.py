import heapq
from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        heap = []
        ans = float('inf')
        for i, num in enumerate(nums[1:-1]):
            heapq.heappush(heap, (num, i + 1))

        while heap:
            mid, j = heapq.heappop(heap)
            left = min(nums[:j])
            if left >= mid:
                continue

            right = min(nums[j+1:])
            if right < mid:
                ans = min(ans, left + mid + right)

        return -1 if ans == float('inf') else ans

    def minimumSum0(self, nums: List[int]) -> int:
        n = len(nums)
        res = mn = 1000
        left = [0] * n
        for i in range(1, n):
            left[i] = mn = min(nums[i - 1], mn)
        right = nums[n - 1]
        for i in range(n - 2, 0, -1):
            if left[i] < nums[i] and nums[i] > right:
                res = min(res, left[i] + nums[i] + right)
            right = min(right, nums[i])
        return res if res < 1000 else -1

    def minimumSum1(self, nums: List[int]) -> int:
        n = len(nums)
        f, fs = float('inf'), [0] * n
        b, bs = float('inf'), [0] * n
        for i, num in enumerate(nums):
            f = min(f, num)
            fs[i] = f

        for i in range(n - 1, -1, -1):
            b = min(b, nums[i])
            bs[i] = b

        ans = float('inf')
        for j, mid in enumerate(nums[1:-1]):
            left = fs[j]
            if left >= mid:
                continue

            right = bs[j+2]
            if right < mid:
                ans = min(ans, left + mid + right)

        return -1 if ans == float('inf') else ans

    def minimumSum2(self, nums: List[int]) -> int:
        n = len(nums)
        b, bs = 51, [51] * (n + 1)
        for i in range(n - 1, -1, -1):
            b = min(b, nums[i])
            bs[i] = b

        f, ans = nums[0], 148
        for i in range(n - 1):
            f = min(f, nums[i])
            if f >= nums[i+1]:
                continue

            if bs[i+2] < nums[i+1]:
                ans = min(ans, f + nums[i+1] + bs[i+2])

        return -1 if ans == 148 else ans
