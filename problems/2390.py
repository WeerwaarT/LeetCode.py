class Solution:
    def removeStars(self, s: str) -> str:
        queue = []
        for c in s:
            if c != '*':
                queue.append(c)
            else:
                queue.pop()

        return ''.join(queue)


if __name__ == '__main__':
    print(Solution().removeStars("leet**cod*e"))
    print(Solution().removeStars("erase*****"))
