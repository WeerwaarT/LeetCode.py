# 1448. 统计二叉树中好节点的数目
# https://leetcode.cn/problems/count-good-nodes-in-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, biggest_val: int) -> int:
            count =  1 if node.val >= biggest_val else 0
            biggest_val = node.val if count else biggest_val

            if node.left:
                count += dfs(node.left, biggest_val)

            if node.right:
                count += dfs(node.right, biggest_val)

            return count

        return dfs(root, root.val - 1)