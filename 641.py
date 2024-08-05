class MyCircularDeque:

    def __init__(self, k: int):
        self.array = [-1] * k
        self.size = 0
        self.front = 0
        self.rear = 0
        self.max_length = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.array[self.front] = value
            self.size += 1
            return True

        self.front = (self.front - 1) % self.max_length
        self.array[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.array[self.rear] = value
            self.size += 1
            return True

        self.rear = (self.rear + 1) % self.max_length
        self.array[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.size -= 1
        if not self.isEmpty():
            self.front = (self.front + 1) % self.max_length

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.size -= 1
        if not self.isEmpty():
            self.rear = (self.rear - 1) % self.max_length

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.array[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.array[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_length
