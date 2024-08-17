class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        different_index = -1
        first = False
        for i in range(len(s1)):
            if s1[i] != s2[i] and not first:
                different_index = i
                first = True
            else:
                s1 = s1[:different_index] + s1[i] + s1[different_index + 1: i] + s1[different_index] + s1[i + 1:]
                print(s1)
                return s1 == s2

        return s1 == s2


Solution().areAlmostEqual("bank", "kanb")
