import pytest
from main.ds.linkedList.StackWithLinkedList import StackWithLinkedList


def testPushSingle():
    stack = StackWithLinkedList()
    stack.push(10)
    assert stack.pop() == 10

def testPushMultiple():
    stack = StackWithLinkedList()
    for i in range(10):
        stack.push(i)

    j = 9
    while j >= 0:
        stack.pop() == j
        j -= 1

