from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for log in logs:
            operation = log.split('/')[0]
            if operation == "..":
                level = max(0, level - 1)
            elif operation == ".":
                continue
            else:
                level += 1

        return level

    def minOperations_(self, logs: List[str]) -> int:
        n = 0
        for log in logs:
            if log == './':
                pass
            elif log == '../':
                n -= 1
            else:
                n += 1
            n = max(n, 0)
        return n
