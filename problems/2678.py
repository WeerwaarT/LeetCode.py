# 2678. 老人的数目
# https://leetcode.cn/problems/number-of-senior-citizens/
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                count += 1

        return count
