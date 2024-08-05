# 337. 打家劫舍 III
# https://leetcode.cn/problems/house-robber-iii/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> (int, int):
            if not (node.left or node.right):
                return node.val, 0

            g0_left, g1_left = dfs(node.left) if node.left else (0, 0)
            g0_right, g1_right = dfs(node.right) if node.right else (0, 0)
            g1 = g0_left + g0_right
            g0 = max(g1, g1_left + g1_right + node.val)
            return g0, g1

        return dfs(root)[0]

    # def rob(self, root: Optional[TreeNode]) -> int:
    #     def dfs(node: TreeNode) -> (int, int):
    #         if node.left:
    #             g0_left, g1_left = dfs(node.left)
    #             if node.right:
    #                 g0_right, g1_right = dfs(node.right)
    #                 g1 = g0_left + g0_right
    #                 g0 = max(g1, g1_left + g1_right + node.val)
    #                 return g0, g1
    #             else:
    #                 return max(g0_left, g1_left + node.val), g0_left
    #
    #         if node.right:
    #             g0_right, g1_right = dfs(node.right)
    #             return max(g0_right, g1_right + node.val), g0_right
    #
    #         return node.val, 0
    #
    #     return dfs(root)[0]
