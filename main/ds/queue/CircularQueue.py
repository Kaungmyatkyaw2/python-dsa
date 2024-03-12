from main.ds.queue.Queue import (
    ArrayBasedQueue,
    QueueOverflowException,
    QueueUnderflowException,
)


class CircularQueue(ArrayBasedQueue):
    def __init__(self, maxSize):
        self.rear = -1
        self.front = -1
        self.maxSize = maxSize
        self.items = [0] * maxSize
        self.noOfItems = 0

    def enque(self, item):
        if not self.isFull():
            self.noOfItems += 1
            self.rear = (self.rear + 1) % self.maxSize
            self.items[self.rear] = item
        else:
            raise QueueOverflowException("Queue Overflow.")

    def deque(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.maxSize
            self.noOfItems -= 1
            showItem = self.items[self.front]
            # self.items[self.front] = None
            return showItem

        else:
            raise QueueUnderflowException("Queue underflow.")
