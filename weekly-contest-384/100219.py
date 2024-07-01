from collections import Counter
from heapq import heapify, heappop
from typing import List

class Solution:
    # 我自己没写出来
    # def maxPalindromesAfterOperations(self, words: List[str]) -> int:
    #     pass

    # 聪明捏
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        n = len(words)
        cnt = Counter(c for w in words for c in w)
        v = sum(x % 2 for x in cnt.values())

        nums = [-len(w) for w in words]
        for i in range(n):
            if nums[i] % 2:
                nums[i] += 1
                v -= 1

        heapify(nums)
        ans = n
        # 最多执行 O(|Σ|) 次的循环
        while v > 0:
            v += heappop(nums)
            ans -= 1
        return ans

    # 都好厉害啊
    # def maxPalindromesAfterOperations(self, words: List[str]) -> int:
    #     ans = 0
    #     count = 0
    #     for x in Counter("".join(words)).values():
    #         count += x // 2
    #     for pi in sorted([len(word) for word in words]):
    #         if count >= pi // 2:
    #             count -= pi // 2
    #             ans += 1
    #     return ans
