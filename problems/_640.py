class Solution:
    def solveEquation(self, equation: str) -> str:
        # ax + b = 0 -> x = -b / a
        a = 0
        b = 0
        number = ""
        left_hand_side = True

        for i in equation:
            if left_hand_side:
                if i == 'x':
                    if number == "":
                        a += 1
                    else:
                        a += int(number)
                        number = ""
                elif i == '+' or i == '-':
                    if number == "":
                        number += i
                    else:
                        b += int(number)
                        number = i
                else:
                    number += i
            else:
                pass

