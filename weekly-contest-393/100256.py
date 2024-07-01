class Solution:
    def findLatestTime(self, s: str) -> str:
        ans = []
        for i, c in enumerate(s):
            if c != '?':
                ans.append(c)
                continue

            if i == 0:
                if s[1] == '?' or int(s[1]) < 2:
                    ans.append('1')
                else:
                    ans.append('0')
            elif i == 1:
                if ans[0] == '0':
                    ans.append('9')
                else:
                    ans.append('1')
            elif i == 3:
                ans.append('5')
            else:
                ans.append('9')

        return ''.join(ans)


if __name__ == '__main__':
    print(Solution().findLatestTime('?3:12'))
