from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n, left, right = len(nums), 0, 0
        ans = 0
        last = -1
        while right < n:
            cur = nums[right]
            if cur != last:
                right += 1
                last = cur
                if right >= n:
                    length = right - left
                    ans += length * (length + 1) // 2
            else:
                length = right - left
                ans += length * (length + 1) // 2
                left = right
                last = -1

        return ans


if __name__ == '__main__':
    print(Solution().countAlternatingSubarrays([0, 1, 1, 1]))
    print(Solution().countAlternatingSubarrays([1, 0, 1, 0]))
