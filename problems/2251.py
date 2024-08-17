# 2251. 花期内花的数目
# https://leetcode.cn/problems/number-of-flowers-in-full-bloom/
import collections
from typing import List


class Solution:
    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/number-of-flowers-in-full-bloom/solutions/2457828/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        cnt = collections.defaultdict(int)
        for start, end in flowers:
            cnt[start] += 1
            cnt[end + 1] -= 1
        arr = sorted(cnt.items())
        m = len(people)
        ans = [0] * m
        j, curr = 0, 0
        for p, i in sorted(zip(people, range(m))):
            while j < len(arr) and arr[j][0] <= p:
                curr += arr[j][1]
                j += 1
            ans[i] = curr
        return ans
