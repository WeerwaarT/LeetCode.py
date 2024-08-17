from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([(0, root)])
        max_depth = 0
        result = 0
        flag = False

        while len(queue):
            temp = queue.pop()

            if temp[1].left:
                queue.append((temp[0] + 1, temp[1].left))
                flag = True

            if temp[1].right:
                queue.append((temp[0] + 1, temp[1].right))
                flag = True

            if flag:
                flag = False
                continue

            if temp[0] > max_depth:
                max_depth = temp[0]
                result = temp[1].val
            elif temp[0] == max_depth:
                result += temp[1].val

        return result

    def _deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        Q = deque([q])
        while Q:
            p = Q.popleft()
            temp = []
            for i in p:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if temp:
                Q.append(temp)
            else:
                result = 0
                for i in p:
                    result += i.val
                return result
