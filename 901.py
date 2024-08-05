# 901. 股票价格跨度
# https://leetcode.cn/problems/online-stock-span/
from math import inf


class StockSpanner:
    def __init__(self):
        self.stack = [(-1, inf)]
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1
        while price >= self.stack[-1][1]:
            self.stack.pop()
        self.stack.append((self.idx, price))
        return self.idx - self.stack[-2][0]
