from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        my_dict = {}
        dummy = TreeNode(0, root)
        q = [(-1, dummy)]
        while (x not in my_dict) or (y not in my_dict):
            temp = []
            for depth, cur in q:
                if cur.left:
                    temp.append((depth + 1, cur.left))
                    my_dict[cur.left.val] = (depth + 1, cur.val)

                if cur.right:
                    temp.append((depth + 1, cur.right))
                    my_dict[cur.right.val] = (depth + 1, cur.val)

            q = temp

        return (my_dict[x][0] == my_dict[y][0]) and (my_dict[x][1] != my_dict[y][1])
