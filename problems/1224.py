from collections import Counter, defaultdict
from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        counter1 = Counter(nums)

        while len(nums):
            counter1 = +counter1
            counter2 = Counter(counter1.values())
            frequecies = sorted([key for key in counter2.keys()])
            if len(frequecies) == 2 \
                    and ((counter2[frequecies[1]] == 1 and frequecies[1] - frequecies[0] == 1)
                         or (counter2[frequecies[0]] == 1 and frequecies[0] == 1)):
                return len(nums)
            elif len(frequecies) == 1 and (frequecies[0] == 1 or counter2[frequecies[0]] == 1):
                return len(nums)

            counter1[nums.pop()] -= 1

        return 1

    def _maxEqualFreq(self, nums: List[int]) -> int:
        # 按数字查次数
        n_cnt = Counter(nums)

        # 按次数查数字
        cnt_n = defaultdict(set)
        for key in n_cnt.keys():
            val = n_cnt[key]
            cnt_n[val].add(key)

        n = len(nums)
        while n > 0:
            # print(cnt_n)
            if len(cnt_n) == 1:
                a = list(cnt_n.keys())[0]
                # 计数都是1
                if a == 1:
                    return n

                # 该计数对应的数字只有一个
                if len(cnt_n[a]) == 1:
                    return n

            if len(cnt_n) == 2:
                tmp = list(cnt_n.keys())
                a, b = tmp
                if a > b:
                    a, b = b, a

                if a + 1 == b and len(cnt_n[b]) == 1:
                    return n

                if a == 1 and len(cnt_n[a]) == 1:
                    return n

            # 去除末尾一个数字
            num = nums[n - 1]
            # 数字-计数 字典 减一
            cur_cnt = n_cnt[num]
            n_cnt[num] = cur_cnt - 1

            # 计数-数字 字典
            # 去除原计数数字
            if len(cnt_n[cur_cnt]) == 1:
                del cnt_n[cur_cnt]
            else:
                cnt_n[cur_cnt].remove(num)

                # 若去除后计数不为0，添加新计数
            if cur_cnt > 1:
                cnt_n[cur_cnt - 1].add(num)

                # 末尾左移
            n -= 1
