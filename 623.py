from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.depth = 0
        self.val = 0

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val=val)
            new_root.left = root
            return new_root

        self.depth = depth
        self.val = val
        self.dfs(current_depth=1, node=root)
        return root

    def dfs(self, current_depth: int, node: TreeNode):
        if node is None:
            return

        if current_depth == self.depth - 1:
            new_node_left = TreeNode(val=self.val)
            new_node_right = TreeNode(val=self.val)
            new_node_left.left = node.left
            new_node_right.right = node.right
            node.left = new_node_left
            node.right = new_node_right
            return

        self.dfs(current_depth=current_depth + 1, node=node.left)
        self.dfs(current_depth=current_depth + 1, node=node.right)
