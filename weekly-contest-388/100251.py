from typing import List


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        answer = []
        for a, s1 in enumerate(arr):
            ans = ''
            m = len(s1)
            for i in range(m):
                for j in range(i + 1, m + 1):
                    s3 = s1[i:j]
                    found_common = False
                    for b, s2 in enumerate(arr):
                        if a == b:
                            continue

                        if s3 in s2:
                            found_common = True
                            break

                    if not found_common and ans == '':
                        ans = s3
                    elif not found_common:
                        if len(s3) < len(ans):
                            ans = s3
                        elif len(s3) == len(ans):
                            ans = s3 if s3 < ans else ans

            answer.append(ans)

        return answer


if __name__ == '__main__':
    print(Solution().shortestSubstrings(["cab", "ad", "bad", "c"]))
    print(Solution().shortestSubstrings(["abc", "bcd", "abcd"]))
    print(Solution().shortestSubstrings(["gfnt", "xn", "mdz", "yfmr", "fi", "wwncn", "hkdy"])) # ["g","x","z","r","i","c","h"]
