import pytest
from main.ds.linkedList.QueueWithLinkedList import QueueWithLinkedList




def testEnqueDequeOne():
    queue = QueueWithLinkedList()

    queue.enque(10)
    assert queue.isEmpty() == False

    ele = queue.deque()
    assert ele == 10
    assert queue.isEmpty() == True


def testEnqueDequeMany():
    queue = QueueWithLinkedList()

    for i in range(1, 6):
        queue.enque(i * 10)

    assert queue.isEmpty() == False

    for i in range(1, 6):
        assert queue.deque() == i * 10

    assert queue.isEmpty() == True