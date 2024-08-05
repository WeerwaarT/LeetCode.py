class Solution:
    def reformat(self, s: str) -> str:
        digit_list = []
        char_list = []
        for i in s:
            if i in "0123456789":
                digit_list.append(i)
            else:
                char_list.append(i)

        if abs(len(digit_list) - len(char_list)) > 1:
            return ""

        result = [""] * (len(digit_list) + len(char_list))
        if len(digit_list) > len(char_list):
            result[::2] = digit_list
            result[1::2] = char_list
        else:
            result[::2] = char_list
            result[1::2] = digit_list

        return "".join(result)
