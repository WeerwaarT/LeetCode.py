class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        if k == 0:
            return s

        t = []
        for c in s:
            if k == 0:
                t.append(c)
                continue

            forward_distance = abs(ord(c) - ord('a'))
            backward_distance = 26 - forward_distance
            distance = min(forward_distance, backward_distance)
            if k >= distance:
                t.append('a')
                k -= distance
            else:
                t.append(chr(ord(c) - k))
                k = 0

        return ''.join(t)
