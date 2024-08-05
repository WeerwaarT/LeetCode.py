from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        my_dict1 = defaultdict(list)

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return

            nonlocal my_dict1
            if node.left and node.right:
                my_dict1[depth].append(node.left)
                my_dict1[depth].append(node.right)

            if not (node.left and node.right):
                my_dict1[depth].append(node)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root.left, 1)
        dfs(root.right, 1)

        my_dict2 = defaultdict(list)
        for v in my_dict1.values():
            for n in v:
                my_dict2[n.val].append(n)

        ans = []

        def tree_compare(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
            if not tree1:
                if not tree2:
                    return True
                else:
                    return False

            if not tree2:
                return False

            if tree1.val != tree2.val:
                return False

            if not tree_compare(tree1.left, tree2.left):
                return False

            if not tree_compare(tree1.right, tree2.right):
                return False

            return True

        for v in my_dict1.values():
            while len(v) > 1:
                j = 1
                duplicate = False
                while j < len(v):
                    if tree_compare(v[0], v[j]):
                        duplicate = True
                        v.pop(j)
                        continue

                    j += 1

                if duplicate:
                    ans.append(v[0])

                v.pop(0)

        return ans
