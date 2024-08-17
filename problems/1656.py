from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.array = [""] * (n + 2)
        self.left = 1
        self.right = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.array[idKey] = value
        self.left = self.right
        while self.array[self.right]:
            self.right += 1

        return self.array[self.left:self.right]
