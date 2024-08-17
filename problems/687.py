from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.stack: [TreeNode] = []
        self.longest_length: int = 0

    def dfs(self, node: Optional[TreeNode], uni_value: int) -> int:
        if node.val != uni_value:
            self.stack.append(node)
            return -1

        left = 0
        right = 0

        if node.left:
            left = 1 + self.dfs(node.left, uni_value)

        if node.right:
            right = 1 + self.dfs(node.right, uni_value)

        if left and right:
            self.longest_length = max(self.longest_length, left + right)

        return max(left, right)

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.stack.append(root)

        while self.stack:
            node = self.stack.pop()
            current_uni_value = node.val
            self.longest_length = max(self.dfs(node, current_uni_value), self.longest_length)

        return self.longest_length

    def longestUnivaluePath_(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def subTree(node: TreeNode) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                return 0
            c = 0
            d = 0
            if node.left and node.val == node.left.val:
                d = subTree(node.left) + 1
                c += d
            else:
                subTree(node.left)
            if node.right and node.val == node.right.val:
                t = subTree(node.right) + 1
                d = max(d, t)
                c += t
            else:
                subTree(node.right)
            if c > self.max:
                self.max = c
            return d

        subTree(root)
        return self.max

    def longestUnivaluePath__(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left1 = left + 1 if node.left and node.left.val == node.val else 0
            right1 = right + 1 if node.right and node.right.val == node.val else 0
            nonlocal ans
            ans = max(ans, left1 + right1)
            return max(left1, right1)

        dfs(root)
        return ans


print(Solution().longestUnivaluePath(
    TreeNode(1, right=TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, TreeNode(1))))))
