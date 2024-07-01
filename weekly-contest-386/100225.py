from typing import List


class Solution:
    # 我写的太烂了，还用了AI
    # def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
    #     largest, n = 0, len(bottomLeft)
    #     for i in range(n):
    #         for j in range(n):
    #             if i == j:
    #                 continue
    #
    #             Ax1, Ay1 = bottomLeft[i]
    #             Ax2, Ay2 = topRight[i]
    #             Bx1, By1 = bottomLeft[j]
    #             Bx2, By2 = topRight[j]
    #             if (Ax1 < Bx2) and (Ax2 > Bx1) and (Ay1 < By2) and (Ay2 > By1):
    #                 intersect_left_x = max(Ax1, Bx1)
    #                 intersect_bottom_y = max(Ay1, By1)
    #                 intersect_right_x = min(Ax2, Bx2)
    #                 intersect_top_y = min(Ay2, By2)
    #
    #                 # 计算交集区域的宽度和高度
    #                 width = intersect_right_x - intersect_left_x
    #                 height = intersect_top_y - intersect_bottom_y
    #
    #                 # 判断两个矩形是否相交
    #                 if width <= 0 or height <= 0:
    #                     return 0  # 不相交
    #
    #                 # 计算能放入的最大正方形面积
    #                 side_length = min(width, height)
    #                 largest = max(largest, side_length ** 2)
    #
    #     return largest

    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                x0 = max(bottomLeft[i][0], bottomLeft[j][0])
                y0 = max(bottomLeft[i][1], bottomLeft[j][1])
                x1 = min(topRight[i][0], topRight[j][0])
                y1 = min(topRight[i][1], topRight[j][1])
                a = min(x1 - x0, y1 - y0)
                a = max(a, 0)
                ans = max(ans, a ** 2)

        return ans

    # def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
    #     ans = 0
    #     for i in range(len(bottomLeft)):
    #         x1, y1 = bottomLeft[i]
    #         x2, y2 = topRight[i]
    #         for j in range(i + 1, len(bottomLeft)):
    #             x3, y3 = bottomLeft[j]
    #             x4, y4 = topRight[j]
    #             dx = min(x2, x4) - max(x1, x3)
    #             dy = min(y2, y4) - max(y1, y3)
    #             ans = max(ans, min(dx, dy))
    #     return ans ** 2


if __name__ == "__main__":
    print(Solution().largestSquareArea([[1, 2], [1, 2]], [[4, 5], [2, 3]]))
