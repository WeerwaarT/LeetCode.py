class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")

        for i in range(len(words)):
            if words[i].startswith(searchWord):
                return i + 1

        return -1

    def _isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(' '), 1):
            if word.startswith(searchWord):
                return i
        return -1
