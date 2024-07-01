from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            ans.extend(list(filter(lambda x: x != '', word.split(separator))))

        return ans
