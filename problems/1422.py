class Solution:
    def maxScore(self, s: str) -> int:
        zero_count = one_count = 0
        zeros = []
        ones = []

        for c in s[:-1]:
            if c == '0':
                zero_count += 1

            zeros.append(zero_count)

        for i in range(len(s) - 1, 0, -1):
            if s[i] == '1':
                one_count += 1

            ones.append(one_count)

        score = 0
        for i in range(len(s) - 1):
            score = max(score, zeros[i] + ones[-1 - i])

        return score

    def _maxScore(self, s: str) -> int:
        ans = score = (s[0] == '0') + s[1:].count('1')
        for c in s[1:-1]:
            score += 1 if c == '0' else -1
            ans = max(ans, score)
        return ans
