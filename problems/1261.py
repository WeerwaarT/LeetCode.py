import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        queue = collections.deque([self.root])
        while queue:
            cur_node = queue.popleft()
            if cur_node.left:
                cur_node.left.val = cur_node.val * 2 + 1
                queue.append(cur_node.left)

            if cur_node.right:
                cur_node.right.val = cur_node.val * 2 + 2
                queue.append(cur_node.right)

    def find(self, target: int) -> bool:
        def dfs_find(node: TreeNode) -> bool:
            if node.val == target:
                return True

            if node.left and dfs_find(node.left):
                return True

            if node.right and dfs_find(node.right):
                return True

            return False

        return dfs_find(self.root)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)