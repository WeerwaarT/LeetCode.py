# 2003. 每棵子树内缺失的最小基因值
# https://leetcode.cn/problems/smallest-missing-genetic-value-in-each-subtree/
import collections
from typing import List


class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        subtrees = collections.defaultdict(list)
        n = len(parents)
        ans = [0 for _ in range(n)]
        for i in range(1, n):
            subtrees[parents[i]].append(i)

        def dfs(st: int) -> (int, int):
            pass

        dfs(0)
        return ans


if __name__ == '__main__':
    print(Solution().smallestMissingValueSubtree([-1, 0, 0, 2], [1, 2, 3, 4]))
