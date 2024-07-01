class Solution:
    def minOperations(self, k: int) -> int:
        add, mul = k - 1, 0
        min_op = add
        while add >= mul:
            mul += 1
            add = k // mul
            add += 0 if mul * add < k else -1
            min_op = min(min_op, add + mul)

        return min_op
