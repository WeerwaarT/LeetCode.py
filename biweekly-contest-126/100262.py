from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(code: int) -> int:
            s = str(code)
            n = len(s)
            max_digit = 0
            while code:
                max_digit = max(max_digit, code % 10)
                code //= 10

            return int(str(max_digit) * n)

        return sum([encrypt(num) for num in nums])


if __name__ == '__main__':
    print(Solution().sumOfEncryptedInt([10, 21, 31]))
    print(Solution().sumOfEncryptedInt([1, 2, 3]))
