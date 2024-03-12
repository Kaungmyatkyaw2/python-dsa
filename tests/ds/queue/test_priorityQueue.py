import pytest
from main.ds.queue.PriorityQueue import (
    PriorityQueue,
)
from random import randint


def testPriorityQueueBaseCase():

    queue = PriorityQueue(5)
    queue.enque(2)
    queue.enque(20)
    queue.enque(12)
    queue.enque(234)
    queue.enque(244)

    ele = queue.deque()
    print(queue.items)

    for i in range(1, 4):
        dequedEle = queue.deque()
        assert ele >= dequedEle
        ele = dequedEle
    print(queue.items)
    queue.enque(3)
    print(queue.items)

    # assert queue.deque() == 244
