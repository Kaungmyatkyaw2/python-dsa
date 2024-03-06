class QueueOverflowException(Exception):
    def __init__(self, message):
        super().__init__(message)

class QueueUnderflowException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ArrayBasedQueue:
    def __init__(self, maxSize):
        self.front = 0
        self.rear = -1
        self.maxSize = maxSize
        self.items = []
        self.noOfItems = 0

    def enque(self, item):
        if(self.rear < self.maxSize - 1):
            self.rear += 1
            self.items = self.items[0 : self.rear] + [item]
            self.noOfItems += 1
        else:
            raise QueueOverflowException("Queue is full.")

    def deque(self):
        if self.front <= self.rear:
            temp = self.front
            self.front += 1
            self.noOfItems -= 1
            return self.items[temp]
        else:
            raise QueueUnderflowException("Queue is underflow.")

    def getSize(self):
        return self.noOfItems

    def isEmpty(self):
        return self.noOfItems == 0

    def isFull(self):
        return self.noOfItems == self.maxSize