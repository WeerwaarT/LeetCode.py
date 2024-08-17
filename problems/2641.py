from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy_node = TreeNode(left=root)
        queue = [dummy_node]
        total = root.val
        while queue:
            temp = []
            subtotal = 0
            for cur in queue:
                if cur.left:
                    if cur.right:
                        cur.left.val = cur.right.val = cur.left.val + cur.right.val

                    subtotal += cur.left.val
                    temp.append(cur.left)

                if cur.right:
                    temp.append(cur.right)
                    if not cur.left:
                        subtotal += cur.right.val

                cur.val = -cur.val + total

            queue = temp
            total = subtotal

        return dummy_node.left

    # def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     q = [root]
    #     root.val = 0
    #     while len(q) > 0:
    #         q2 = []
    #         sum = 0
    #         for fa in q:
    #             if fa.left:
    #                 q2.append(fa.left)
    #                 sum += fa.left.val
    #             if fa.right:
    #                 q2.append(fa.right)
    #                 sum += fa.right.val
    #         for fa in q:
    #             childSum = (fa.left.val if fa.left else 0) + (fa.right.val if fa.right else 0)
    #             if fa.left:
    #                 fa.left.val = sum - childSum
    #             if fa.right:
    #                 fa.right.val = sum - childSum
    #         q = q2
    #     return root


if __name__ == '__main__':
    Solution().replaceValueInTree(TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(10)), TreeNode(9, right=TreeNode(7))))
