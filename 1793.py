from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = [(nums[k], k)], [(nums[k], k)]
        for i in range(k):
            left.append((nums[i], i))

        for i in range(k + 1, n):
            right.append((nums[i], i))

        left.sort()
        right.sort()


if __name__ == '__main__':
    print(Solution().maximumScore([1, 4, 3, 7, 4, 5], 3))
