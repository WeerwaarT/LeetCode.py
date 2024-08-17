class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces = text.count(" ")
        if len(words) > 1:
            return (spaces // (len(words) - 1) * " ").join(words) + (spaces % (len(words) - 1) * " ")
        else:
            return words[0] + (spaces * " ")

    def _reorderSpaces(self, text: str) -> str:
        spaceNum = text.count(" ")
        wordArr = text.split()
        wordNums = len(wordArr)
        if wordNums == 1:
            strRes = wordArr[0] + " " * spaceNum
        else:
            num, mod = divmod(spaceNum, wordNums - 1)
            strRes = (" " * num).join(wordArr) + " " * mod
        return strRes


print(Solution().reorderSpaces(" practice   makes   perfect"))
