import collections


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d = collections.defaultdict(int)
        max_length = 0
        q = collections.deque()
        for c in s:
            if d[c] < 2:
                q.append(c)
                max_length = max(max_length, len(q))
                d[c] += 1
            else:
                while d[c] >= 2:
                    left = q.popleft()
                    d[left] -= 1

                q.append(c)
                max_length = max(max_length, len(q))
                d[c] += 1

        return max_length


if __name__ == '__main__':
    print(Solution().maximumLengthSubstring("bcbbbcba"))
    print(Solution().maximumLengthSubstring("aaaa"))
    print(Solution().maximumLengthSubstring("eebadadbfa"))
