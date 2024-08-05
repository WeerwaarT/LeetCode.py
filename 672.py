class Solution:
    def flipLights(self, n: int, presses: int) -> int:  # 垃圾题目  面向结果编程
        if presses == 0:
            return 1

        if n == 1:
            return 2

        if n == 2:
            return 3 if presses == 1 else 4

        if presses == 1:
            return 4

        if presses == 2:
            return 7

        return 8

    def flipLights_(self, n: int, presses: int) -> int:
        seen = set()
        for i in range(2 ** 4):
            pressArr = [(i >> j) & 1 for j in range(4)]
            if sum(pressArr) % 2 == presses % 2 and sum(pressArr) <= presses:
                status = pressArr[0] ^ pressArr[1] ^ pressArr[3]
                if n >= 2:
                    status |= (pressArr[0] ^ pressArr[1]) << 1
                if n >= 3:
                    status |= (pressArr[0] ^ pressArr[2]) << 2
                if n >= 4:
                    status |= (pressArr[0] ^ pressArr[1] ^ pressArr[3]) << 3
                seen.add(status)
        return len(seen)
