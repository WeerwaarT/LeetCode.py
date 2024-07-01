import heapq
from typing import List


class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        if 1 in nums:
            nums = [num for num in nums if num == 1]
        else:
            s = list(set(nums))
            for i in range(len(s)):
                for j in range(len(s)):
                    if i != j:
                        # 检查是否能通过模运算得到1
                        if s[i] % s[j] == 1:
                            return 1

        nums = [-num for num in nums]
        heapq.heapify(nums)
        count_0 = 0
        temp_stack = []  # 用于存放暂时移除的元素

        while len(nums) > 1:
            first = -heapq.heappop(nums)
            # 特殊情况处理
            if first == 0:
                count_0 += 1
                break
            # 循环找到一个与first不同的second
            while nums:
                second = -heapq.heappop(nums)
                if second != first:
                    break
                temp_stack.append(second)  # 存储相同的元素

            if second == 0:
                count_0 += 1
                mod_result = first
            elif second == 1:
                mod_result = 1 % first
            else:
                mod_result = second % first

            # 将结果和之前暂存的元素放回堆中
            heapq.heappush(nums, -mod_result)
            while temp_stack:
                heapq.heappush(nums, -temp_stack.pop())

        return len(nums) + count_0


if __name__ == '__main__':
    print(Solution().minimumArrayLength([1, 4, 3, 1]))
    print(Solution().minimumArrayLength([1, 1, 1, 1, 1, 1, 1, 1]))
    print(Solution().minimumArrayLength([4, 4, 4]))
    print(Solution().minimumArrayLength([4, 4]))
    print(Solution().minimumArrayLength([3, 3, 1]))
    print(Solution().minimumArrayLength([5, 3, 10, 10]))
    print(Solution().minimumArrayLength([4, 6, 2, 6, 4]))
