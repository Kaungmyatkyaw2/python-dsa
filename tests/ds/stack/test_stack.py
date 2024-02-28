import pytest
from main.ds.stack.Stack import Stack, StackOverflowException, StackUnderflowException


def testPushSingle():
    stack = Stack(10)
    stack.push(10)
    assert stack.peek() == 10


def testPushMultiple():
    stack = Stack(10)
    for i in range(10):
        stack.push(i)

    j = stack.getSize() - 1
    while j >= 0:
        assert stack.pop() == j
        j -= 1


def testPushStackFullException():
    stack = Stack(10)
    for i in range(10):
        stack.push(i)

    with pytest.raises(StackOverflowException):
        stack.push(11)

    assert stack.isFull() == True


def testPopSingle():
    stack = Stack(10)
    stack.push(100)

    orgSize = stack.getSize()

    assert stack.pop() == 100
    assert orgSize - 1 == 0


def testPopStackUnderflowException():
    stack = Stack(10)
    with pytest.raises(StackUnderflowException):
        stack.pop()
    assert stack.isEmpty() == True
