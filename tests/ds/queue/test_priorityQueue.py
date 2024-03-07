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

    for i in range(1, 5):
        dequedEle =  queue.deque();
        assert ele >= dequedEle
        ele = dequedEle
    queue.enque(1660)

    assert queue.deque() == 1660
