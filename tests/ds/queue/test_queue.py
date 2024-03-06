import pytest
from main.ds.queue.Queue import ArrayBasedQueue,QueueOverflowException


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

    queue.enque(10)
    queue.enque(20)
    queue.enque(30)
    queue.enque(40)
    queue.enque(50)
    assert queue.getSize() == 5
    assert queue.isEmpty() == False


    assert queue.deque() == 10
    assert queue.deque() == 20
    assert queue.deque() == 30
    assert queue.deque() == 40
    assert queue.deque() == 50
    assert queue.getSize() == 0
    assert queue.isEmpty() == True

    # queue.enque(20)


def testQueueFull():
    queue = ArrayBasedQueue(5)

    queue.enque(10)
    queue.enque(20)
    queue.enque(30)
    queue.enque(40)
    queue.enque(50)
    assert queue.getSize() == 5
    assert queue.isEmpty() == False


    with pytest.raises(QueueOverflowException):
        queue.enque(10)
    assert queue.isFull() == True
    assert queue.deque() == 10
    assert queue.isFull() == False
    with pytest.raises(QueueOverflowException):
        queue.enque(10)
