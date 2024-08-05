import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.height = 0

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        self.findDepth(root, 0)
        res = [[""] * (pow(2, self.height + 1) - 1) for _ in range(self.height + 1)]
        self.construct_res(res, root, 0, (pow(2, self.height + 1) - 2) // 2)
        return res

    def findDepth(self, node: TreeNode, depth: int):
        if node.left:
            self.findDepth(node.left, depth + 1)

        if node.right:
            self.findDepth(node.right, depth + 1)

        if not node.left and not node.right:
            self.height = max(self.height, depth)

    def construct_res(self, res: List[List[str]], node: TreeNode, current_height: int, current_position: int):
        res[current_height][current_position] = str(node.val)
        if node.left:
            self.construct_res(res,
                               node.left,
                               current_height + 1,
                               current_position - pow(2, self.height - current_height - 1))

        if node.right:
            self.construct_res(res,
                               node.right,
                               current_height + 1,
                               current_position + pow(2, self.height - current_height - 1))

    def printTree_(self, root: TreeNode) -> List[List[str]]:

        nodes = []

        _next = collections.deque()
        _next.append(root)
        level = 0
        flag = 1
        while flag:
            flag = 0
            new_next = collections.deque()
            node = []
            level += 1
            while _next:
                tmp = _next.popleft()

                if tmp:
                    node.append(str(tmp.val))
                    if tmp.left or tmp.right:
                        new_next.append(tmp.left)
                        new_next.append(tmp.right)
                        flag = 1
                    else:
                        new_next.append(None)
                        new_next.append(None)
                else:
                    new_next.append(None)
                    new_next.append(None)
                    node.append("")

            nodes.append(node)
            _next = new_next

        print(level, nodes)

        res = [[""] * (2 ** level - 1) for _ in range(level)]
        r = 2 ** level - 1
        for i, line in enumerate(nodes):
            pos = 0
            for node in line:
                res[i][pos + r // 2] = node
                pos += r + 1
            r //= 2

        return res

    def printTree__(self, root: Optional[TreeNode]) -> List[List[str]]:
        def calDepth(node: Optional[TreeNode]) -> int:
            return max(calDepth(node.left) + 1 if node.left else 0, calDepth(node.right) + 1 if node.right else 0)

        height = calDepth(root)

        m = height + 1
        n = 2 ** m - 1
        ans = [[''] * n for _ in range(m)]

        def dfs(node: Optional[TreeNode], r: int, c: int) -> None:
            ans[r][c] = str(node.val)
            if node.left:
                dfs(node.left, r + 1, c - 2 ** (height - r - 1))
            if node.right:
                dfs(node.right, r + 1, c + 2 ** (height - r - 1))

        dfs(root, 0, (n - 1) // 2)
        return ans
