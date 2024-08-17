from typing import List


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])
        mask = [sum(v << j for j, v in enumerate(row)) for i, row in enumerate(matrix)]
        res, limit = 0, 1 << n
        for cur in range(1, limit):
            if cur.bit_count() != numSelect:
                continue
            t = sum((mask[j] & cur) == mask[j] for j in range(m))
            res = max(res, t)
        return res

    # def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #     mask = [sum(v << j for j, v in enumerate(row)) for i, row in enumerate(matrix)]
    #     res, cur = 0, (1 << numSelect) - 1
    #     limit = 1 << n
    #     while cur < limit:
    #         t = sum((mask[j] & cur) == mask[j] for j in range(m))
    #         res = max(res, t)
    #         lb = cur & -cur
    #         r = cur + lb
    #         cur = ((r ^ cur) >> count_trailing_zeros(lb) + 2) | r
    #     return res


if __name__ == '__main__':
    # print(Solution().maximumRows([[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], 2))
    # print(Solution().maximumRows([[1], [0]], 1))
    print(Solution().maximumRows([[1, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 0], [1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 1]], 2))
