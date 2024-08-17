class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.array = [-1] * k
        self.front = 0
        self.rear = 0
        self.count = 0
        self.k = k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        self.array[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.count += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False

        self.array[self.front] = -1
        self.front = (self.front + 1) % self.k
        self.count -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        return self.array[self.front]

    def Rear(self):
        """
        :rtype: int
        """
        return self.array[(self.rear - 1) % self.k]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.count == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.count == self.k
