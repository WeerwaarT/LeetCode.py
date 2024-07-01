import collections
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        my_set = collections.defaultdict(int)
        lengths = set()
        count = 0
        for i, word in enumerate(words):
            n = len(word)
            for length in lengths:
                if length <= n and (w := word[:length]) == word[-length:] and w in my_set:
                    count += my_set[w]

            my_set[word] += 1
            lengths.add(len(word))

        return count


if __name__ == '__main__':
    print(Solution().countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]))
    print(Solution().countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]))
    print(Solution().countPrefixSuffixPairs(["abab", "ab"]))
    print(Solution().countPrefixSuffixPairs(["bb", "bb", "bb"]))
    print(Solution().countPrefixSuffixPairs(["bb", "bb"]))
