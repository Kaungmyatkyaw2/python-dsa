from main.ds.queue.CircularQueue import CircularQueue
from main.ds.queue.Queue import QueueOverflowException


class PriorityQueue(CircularQueue):
    def __init__(self, maxSize):
        super().__init__(maxSize)

    def enque(self, item):
        if not self.isFull():
            super().enque(item)
            if self.noOfItems > 1:
                index = self.rear
                while self.items[index] > self.items[index - 1] and index > 0:
                    [self.items[index - 1], self.items[index]] = [
                        self.items[index],
                        self.items[index - 1],
                    ]
                    index -= 1
        else:
            raise QueueOverflowException("Queue Overflow.")
