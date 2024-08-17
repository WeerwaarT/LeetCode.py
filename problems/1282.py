from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        x = defaultdict(list)
        for i, g in enumerate(groupSizes):
            x[g].append(i)

        result = []
        for k, v in x.items():
            for i in range(0, len(v), k):
                result.append(x[k][i:i + k])

        return result
