from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        if len(nums) == 1:
            return TreeNode(val=nums[0])

        _max = 0
        for i, num in enumerate(nums):
            if num >= nums[_max]:
                _max = i

        root = TreeNode(val=nums[_max],
                        left=self.constructMaximumBinaryTree(nums[:_max]),
                        right=self.constructMaximumBinaryTree(nums[_max + 1:]))

        return root

    def constructMaximumBinaryTree_(self, nums: List[int]) -> TreeNode:
        stack = []
        nums.append(2000)
        for num in nums:
            curr = TreeNode(num)
            while stack and stack[-1].val < num:
                node = stack.pop()
                if stack and stack[-1].val < num:
                    stack[-1].right = node
                else:
                    curr.left = node
            stack.append(curr)
        root = stack.pop()
        return root.left


Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
