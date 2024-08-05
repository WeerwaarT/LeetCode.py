# 2582. 递枕头
# https://leetcode.cn/problems/pass-the-pillow/


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        quo, mod = time // (n - 1), time % (n - 1)
        return n - mod if quo % 2 == 1 else mod + 1

    # def passThePillow(self, n: int, time: int) -> int:
    #     time %= (n - 1) * 2
    #     return time + 1 if time < n else n * 2 - time - 1
    #
    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/pass-the-pillow/solutions/2451117/di-zhen-tou-by-leetcode-solution-kl5e/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == '__main__':
    print(Solution().passThePillow(4, 5))
    print(Solution().passThePillow(3, 2))