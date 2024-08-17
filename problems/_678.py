class Solution:
    def checkValidString(self, s: str) -> bool:
        star_count = 0
        stack = 0

        for i in s:
            if i == '(':
                stack += 1
            elif i == ')':
                stack -= 1
            else:
                star_count += 1

            if stack < 0:
                if star_count > 0:
                    star_count -= 1
                    stack += 1

        if stack == 0:
            return True
        else:
            return star_count >= stack


A = Solution()
print(A.checkValidString("*("))
