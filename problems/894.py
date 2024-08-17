import collections
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.dict = collections.defaultdict(list)
        self.dict[0].append(None)
        self.dict[1].append(TreeNode())

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n in self.dict:
            return self.dict[n]

        for i in range(1, n - 1, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n - i - 1)
            for l in left:
                for r in right:
                    treenode = TreeNode(left=l, right=r)
                    self.dict[n].append(treenode)

        return self.dict[n]


if __name__ == '__main__':
    print(Solution().allPossibleFBT(3))
