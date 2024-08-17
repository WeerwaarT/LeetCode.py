# 1038. 从二叉搜索树到更大和树
# https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(num: int, node: TreeNode) -> int:
            if node.right:
                node.val += dfs(num, node.right)

            if node.left:
                ans = node.val + node.left.val
                dfs(node.val, node.left)
                return ans

            return node.val

        dfs(0, root)
        return root
