from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count_bits(n):
            count = 0
            while n:
                n &= n - 1
                count += 1
            return count

        nn = len(nums)
        for i in range(nn):
            for j in range(0, nn - i - 1):
                if nums[j] <= nums[j + 1]:
                    continue
                else:
                    if count_bits(nums[j]) == count_bits(nums[j + 1]):
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    else:
                        return False

        return True


if __name__ == '__main__':
    print(Solution().canSortArray([1, 2, 3, 4, 5]))
    print(Solution().canSortArray([3, 16, 8, 4, 2]))
    print(Solution().canSortArray([8, 4, 2, 30, 15]))
