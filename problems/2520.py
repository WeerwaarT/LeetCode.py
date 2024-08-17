# 2520. 统计能整除数字的位数
# https://leetcode.cn/problems/count-the-digits-that-divide-a-number/


class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        temp = num
        while temp:
            if num % (temp % 10) == 0:
                count += 1

            temp //= 10

        return count


if __name__ == '__main__':
    print(Solution().countDigits(7))
    print(Solution().countDigits(121))
