import pytest
from main.ds.queue.CircularQueue import (
    CircularQueue,
)


queue = CircularQueue(5)


def testCircularQueueBaseCase():

    for i in range(0, 5):
        queue.enque(i)

    assert queue.getSize() == 5
    assert queue.isEmpty() == False

    for i in range(0, 5):
        assert queue.deque() == i

    queue.enque(10)
    assert queue.getSize() == 1
    assert queue.deque() == 10
