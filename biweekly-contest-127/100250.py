from typing import List


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + (1 if possible[i - 1] == 1 else -1)

        for i in range(1, n):
            a = prefix_sum[i]
            b = prefix_sum[-1] - a
            if a > b:
                return i

        return -1


if __name__ == '__main__':
    print(Solution().minimumLevels([1, 1]))
