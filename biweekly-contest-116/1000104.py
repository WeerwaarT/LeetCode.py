# 100104. 使二进制字符串变美丽的最少修改次数
# https://leetcode.cn/contest/biweekly-contest-116/problems/minimum-number-of-changes-to-make-binary-string-beautiful/


class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        n = len(s) // 2
        for i in range(n):
            if s[2 * i] != s[2 * i + 1]:
                count += 1

        return count


if __name__ == '__main__':
    print(Solution().minChanges('0000'))
    print(Solution().minChanges('1100'))
    print(Solution().minChanges('1001'))
    print(Solution().minChanges('10'))
