class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(" ")
        ans = []
        for word in words:
            if len(word) <= 2:
                ans.append(word.lower())
            else:
                ans.append(word[0].upper() + word[1:].lower())

        return " ".join(ans)


if __name__ == '__main__':
    print(Solution().capitalizeTitle("capiTalIze tHe titLe"))
    print(Solution().capitalizeTitle("heLlo wORLD!"))
    print(Solution().capitalizeTitle("heLlo FROM windows!"))
