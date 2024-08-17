from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)

        if val > root.val:
            new_node.left = root
            return new_node
        else:
            temp = root
            while temp.right and temp.right.val > val:
                temp = temp.right

            new_node.left = temp.right
            temp.right = new_node

            return root
