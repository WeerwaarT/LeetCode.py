class Solution:
    def checkRecord(self, s: str) -> bool:
        # return "LLL" not in s and s.count("A") < 2
        n = len(s)
        absent = False
        late = 0
        for i in range(n):
            if s[i] == "A":
                if absent:
                    return False

                absent = True
            elif s[i] == "L":
                if late == 2:
                    return False

                late += 1
            else:
                late = 0

        return True
