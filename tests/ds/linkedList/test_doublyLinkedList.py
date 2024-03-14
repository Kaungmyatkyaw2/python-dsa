import pytest
from main.ds.linkedList.doublyLinkedList.DoublyNode import DoublyNode
from main.ds.linkedList.doublyLinkedList.DoublyLinkedList import DoublyLinkedList
from main.ds.linkedList.doublyLinkedList.ReverseIterator import ReverseIterator
from main.ds.linkedList.LinkedList import LinkedListIterator


def testInsertFirstEmpty():
    list = DoublyLinkedList()
    first = DoublyNode(10)
    list.insertFirst(first)

    assert list.isEmpty() == False
    assert list.getFirst() == first
    assert list.getLast() == first


def testInsertFirstNonEmpty():
    list = DoublyLinkedList()
    first = DoublyNode(10)
    second = DoublyNode(20)
    third = DoublyNode(30)
    list.insertFirst(first)
    list.insertFirst(second)
    list.insertFirst(third)

    iterator = LinkedListIterator(list)

    ele1 = iterator.next()
    assert ele1 == third

    ele2 = iterator.next()
    assert ele2 == second

    ele3 = iterator.next()
    assert ele3 == first

    assert third.getNext() == second
    assert second.getNext() == first

    assert first.getPrevious() == second
    assert second.getPrevious() == third

    assert list.getFirst() == third
    assert list.getLast() == first

    # assert ele1.getNext() == ele2
    # assert ele2.getPrevious() == ele1

    # assert list.getFirst() == ele1
    # assert list.getLast() == ele2

    assert iterator.hasNext() == False


def testInsertFirstNonEmptyReverseIterator():
    list = DoublyLinkedList()
    first = DoublyNode(10)
    second = DoublyNode(20)
    third = DoublyNode(30)
    list.insertFirst(first)
    list.insertFirst(second)
    list.insertFirst(third)

    iterator = ReverseIterator(list)

    ele1 = iterator.next()
    assert ele1 == first

    ele2 = iterator.next()
    assert ele2 == second

    ele3 = iterator.next()
    assert ele3 == third

    assert iterator.hasNext() == False

    # assert third.getNext() == second
    # assert second.getNext() == first

    # assert first.getPrevious() == second
    # assert second.getPrevious() == third


def testInsertLastEmpty():
    list = DoublyLinkedList()
    first = DoublyNode(10)
    list.insertLast(first)

    assert list.isEmpty() == False
    assert list.getFirst() == first
    assert list.getLast() == first


def testInsertLastNonEmpty():
    list = DoublyLinkedList()
    first = DoublyNode(10)
    second = DoublyNode(20)
    third = DoublyNode(30)
    list.insertLast(first)
    list.insertLast(second)
    list.insertLast(third)

    iterator = LinkedListIterator(list)

    ele1 = iterator.next()
    assert ele1 == first

    ele2 = iterator.next()
    assert ele2 == second

    ele3 = iterator.next()
    assert ele3 == third

    assert first.getNext() == second
    assert second.getNext() == third

    assert third.getPrevious() == second
    assert second.getPrevious() == first

    assert list.getFirst() == first
    assert list.getLast() == third

    # assert ele1.getNext() == ele2
    # assert ele2.getPrevious() == ele1

    # assert list.getFirst() == ele1
    # assert list.getLast() == ele2

    assert iterator.hasNext() == False


def testInsertLastNonEmptyManyNode():
    list = DoublyLinkedList()
    nodes = [0] * 10

    for i in range(10):
        ele =  DoublyNode(i)
        nodes[i] = ele
        list.insertLast(ele)

    iterator = LinkedListIterator(list)

    for i in range(10):
        assert iterator.next() == nodes[i]

    for i in range(1,10):
        prevNode = nodes[i - 1]
        nextNode = nodes[i]
        assert prevNode.getNext() == nextNode
        assert nextNode.getPrevious() == prevNode

    assert list.getFirst() == nodes[0]
    assert list.getLast() == nodes[9]

def testInsertAfterSingleItem():
    list = DoublyLinkedList()
    first = DoublyNode(10)
    second = DoublyNode(20)
    list.insertLast(first)
    list.insertAfter(first,second)

    iterator = LinkedListIterator(list)

    assert iterator.next() == first
    assert iterator.next() == second

    assert list.isEmpty() == False
    assert list.getFirst() == first
    assert list.getLast() == second

def testInsertAfterManyItems():
    list = DoublyLinkedList()
    first = DoublyNode(10)
    second = DoublyNode(20)
    third = DoublyNode(30)
    fourth = DoublyNode(40)
    list.insertLast(first)
    list.insertLast(second)
    list.insertAfter(first,third)
    list.insertAfter(third,fourth)

    iterator = LinkedListIterator(list)

    assert iterator.next() == first
    assert iterator.next() == third
    assert iterator.next() == fourth
    assert iterator.next() == second

    assert list.isEmpty() == False
    assert list.getFirst() == first
    assert list.getLast() == second

    assert first.getNext() == third
    assert third.getNext() == fourth
    assert fourth.getNext() == second

    assert second.getPrevious() == fourth
    assert third.getPrevious() == first
    assert fourth.getPrevious() == third
