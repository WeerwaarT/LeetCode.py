# 1402. 做菜顺序
# https://leetcode.cn/problems/reducing-dishes/
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        non_negatives = [0]
        negatives = []
        for s in satisfaction:
            if s < 0:
                negatives.append(s)
            else:
                non_negatives.append(s)

        like_time_coe_sum = 0
        pre_sum = 0
        for i, nn in enumerate(non_negatives):
            like_time_coe_sum += i * nn
            pre_sum += nn

        for i in range(len(negatives) - 1, -1, -1):
            if pre_sum + negatives[i] <= 0:
                break

            pre_sum += negatives[i]
            like_time_coe_sum += pre_sum

        return like_time_coe_sum

    # 二分并没有更快
    # def maxSatisfaction(self, satisfaction: List[int]) -> int:
    #     satisfaction.sort()
    #     n = len(satisfaction)
    #     left, right = 0, n - 1
    #     while left < right:
    #         mid = (right - left) // 2 + left
    #         if satisfaction[mid] >= 0:
    #             right = mid
    #         else:
    #             left = mid + 1
    #
    #     like_time_coe_sum = 0
    #     pre_sum = 0
    #     time = 1
    #     if satisfaction[left] < 0:  # 第一遍写的没想到可以提前退出
    #         return 0
    #
    #     for j in range(left, n):
    #         like_time_coe_sum += time * satisfaction[j]
    #         pre_sum += satisfaction[j]
    #         time += 1
    #
    #     for i in range(left - 1, -1, -1):
    #         if pre_sum + satisfaction[i] <= 0:
    #             break
    #
    #         pre_sum += satisfaction[i]
    #         like_time_coe_sum += pre_sum
    #
    #     return like_time_coe_sum

    # 牛逼
    # def maxSatisfaction(self, satisfaction: List[int]) -> int:
    #     satisfaction.sort(reverse=True)
    #     ans = s = 0
    #     for x in satisfaction:
    #         s += x
    #         if s <= 0:
    #             break
    #         ans += s
    #     return ans


if __name__ == '__main__':
    print(Solution().maxSatisfaction([-1, -8, 0, 5, -7]))
    print(Solution().maxSatisfaction([4, 3, 2]))
    print(Solution().maxSatisfaction([-1, -4, -5]))
