class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = s.count(c)
        return (count + 1) * count // 2


if __name__ == '__main__':
    print(Solution().countSubstrings("abada", 'a'))
print(Solution().countSubstrings("zzz", 'z'))