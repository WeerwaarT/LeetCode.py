# 2337. 移动片段得到字符串
# https://leetcode.cn/problems/move-pieces-to-obtain-a-string/


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_', '') != target.replace('_', ''):
            return False

        n = len(start)
        left = 0
        for right, s in enumerate(target):
            if s == '_': continue
            while start[left] == '_': left += 1
            if start[left] == 'L' and left < right: return False
            if start[left] == 'R' and left > right: return False
            left += 1

        return left <= n