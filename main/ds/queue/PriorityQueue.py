from main.ds.queue.CircularQueue import CircularQueue
from main.ds.queue.Queue import QueueOverflowException


class PriorityQueue(CircularQueue):
    def __init__(self, maxSize):
        super().__init__(maxSize)

    def getNextLessIndex(self, index):
        nextIndex = index - 1
        if nextIndex < 0:
            return nextIndex + self.maxSize

        return nextIndex

    def enque(self, item):
        if not self.isFull():
            super().enque(item)
            if self.noOfItems > 1:
                index = self.rear
                comparison = 0
                while (
                    comparison < self.noOfItems - 1
                    and self.items[index] > self.items[self.getNextLessIndex(index)]
                ):
                    nextIndex = self.getNextLessIndex(index)  # 0
                    [self.items[nextIndex], self.items[index]] = [
                        self.items[index],
                        self.items[nextIndex],
                    ]
                    index = nextIndex
                    comparison += 1
        else:
            raise QueueOverflowException("Queue Overflow.")
