from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = [arr[0]]

        for num in arr[1:]:
            if num > stack[-1]:
                stack.append(num)
            else:
                top = stack.pop()
                while len(stack):
                    if num > stack[-1]:
                        break

                    stack.pop()

                stack.append(top)

        return len(stack)


print(Solution().maxChunksToSorted([1, 2, 0, 3]))
