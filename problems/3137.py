import collections


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        if k == n:
            return 0

        counter = collections.Counter([word[i:i+k] for i in range(0, n, k)])
        return (n // k) - counter.most_common(1)[0][1]  # n // k - max(counter.values())


if __name__ == '__main__':
    print(Solution().minimumOperationsToMakeKPeriodic("leetcodeleet", 4))
