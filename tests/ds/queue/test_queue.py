import pytest
from main.ds.queue.Queue import (
    ArrayBasedQueue,
    QueueOverflowException,
    QueueUnderflowException,
)


def testEnqueDequeOne():
    queue = ArrayBasedQueue(10)

    queue.enque(10)
    assert queue.getSize() == 1
    assert queue.isEmpty() == False

    ele = queue.deque()
    assert ele == 10
    assert queue.getSize() == 0
    assert queue.isEmpty() == True


def testEnqueDequeMany():
    queue = ArrayBasedQueue(5)

    for i in range(1, 6):
        queue.enque(i * 10)

    assert queue.getSize() == 5
    assert queue.isEmpty() == False

    for i in range(1, 6):
        assert queue.deque() == i * 10

    assert queue.getSize() == 0
    assert queue.isEmpty() == True


def testQueueOverflowException():
    queue = ArrayBasedQueue(5)

    for i in range(1, 6):
        queue.enque(i * 10)

    assert queue.getSize() == 5
    assert queue.isEmpty() == False

    with pytest.raises(QueueOverflowException):
        queue.enque(10)

    assert queue.isFull() == True
    assert queue.deque() == 10
    assert queue.isFull() == False

    with pytest.raises(QueueOverflowException):
        queue.enque(10)


def testQueueUnderflowException():
    queue = ArrayBasedQueue(5)
    for i in range(5):
        queue.enque(i)

    assert queue.getSize() == 5
    assert queue.isEmpty() == False

    for i in range(5):
        assert queue.deque() == i

    with pytest.raises(QueueUnderflowException):
        queue.deque()
