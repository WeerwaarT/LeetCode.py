from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        count = 0
        counter = counter.most_common()
        counter.reverse()
        keys = 8
        press = 1
        while len(counter) > 0:
            count += press * counter.pop()[1]
            keys -= 1
            if keys == 0:
                keys = 8
                press += 1

        return count


if __name__ == '__main__':
    print(Solution().minimumPushes("abcde"))
    print(Solution().minimumPushes("xycdefghij"))
