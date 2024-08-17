# 2525. 根据规则将箱子分类
# https://leetcode.cn/problems/categorize-box-according-to-criteria/


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        if max(length, width, height) >= 10 ** 4 or length * width * height >= 10 ** 9:
            if mass >= 100:
                return 'Both'

            return 'Bulky'

        return 'Heavy' if mass >= 100 else 'Neither'


if __name__ == '__main__':
    print(Solution().categorizeBox(1000, 35, 700, 300))
    print(Solution().categorizeBox(200, 50, 800, 50))