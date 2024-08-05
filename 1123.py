# 1123. 最深叶节点的最近公共祖先
# https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode, depth: int) -> (TreeNode, int):
            if not (node.left or node.right):
                return node, depth

            if not node.left:
                return dfs(node.right, depth + 1)

            if not node.right:
                return dfs(node.left, depth + 1)

            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)
            if left[1] == right[1]:
                return node, left[1]

            if left[1] < right[1]:
                return right
            else:
                return left

        return dfs(root, 0)[0]

    # def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     def f(root):
    #         if not root:
    #             return 0, None
    #
    #         d1, lca1 = f(root.left)
    #         d2, lca2 = f(root.right)
    #
    #         if d1 > d2:
    #             return d1 + 1, lca1
    #         if d1 < d2:
    #             return d2 + 1, lca2
    #         return d1 + 1, root
    #
    #     return f(root)[1]
