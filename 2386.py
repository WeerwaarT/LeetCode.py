import heapq
from typing import List


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            if nums[i] >= 0:
                total += nums[i]
            else:
                nums[i] = -nums[i]
        nums.sort()

        ret = 0
        pq = [(nums[0], 0)]
        for j in range(k - 1):
            t, i = heapq.heappop(pq)
            ret = t
            if i == n - 1:
                continue
            heapq.heappush(pq, (t + nums[i + 1], i + 1))
            heapq.heappush(pq, (t - nums[i] + nums[i + 1], i + 1))
        return total - ret

    # def kSum(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     total, total2 = 0, 0
    #     for i in range(n):
    #         if nums[i] >= 0:
    #             total += nums[i]
    #         else:
    #             nums[i] = -nums[i]
    #         total2 += nums[i]
    #     nums.sort()
    #
    #     cnt = 0
    #
    #     def dfs(i: int, t: int, limit: int) -> int:
    #         nonlocal cnt
    #         if i == n or cnt >= k - 1 or t + nums[i] > limit:
    #             return
    #         cnt += 1
    #         dfs(i + 1, t + nums[i], limit)
    #         dfs(i + 1, t, limit)
    #
    #     left, right = 0, total2
    #     while left <= right:
    #         mid = (left + right) // 2
    #         cnt = 0
    #         dfs(0, 0, mid)
    #         if cnt >= k - 1:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return total - left


if __name__ == '__main__':
    print(Solution().kSum([492634335, 899178915, 230945927], 2))
