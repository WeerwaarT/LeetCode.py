class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reverse = s[::-1]
        print(reverse)
        for i in range(len(s) - 1):
            sub_s = s[i:i+2]
            if sub_s in reverse:
                return True

        return False


if __name__ == '__main__':
    print(Solution().isSubstringPresent("leetcode"))
