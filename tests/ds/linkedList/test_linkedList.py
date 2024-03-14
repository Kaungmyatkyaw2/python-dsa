import pytest
from main.ds.linkedList.LinkedList import LinkedList, LinkedListIterator
from main.ds.linkedList.Node import Node


def testShowAll():
    print("\n")
    one = Node(1)
    two = Node(2)
    three = Node(3)

    linkedList = LinkedList()
    linkedList.insertLast(one)
    linkedList.insertLast(two)
    linkedList.insertLast(three)

    # linkedList.showAll()


def testIterator():
    one = Node(1)
    two = Node(2)
    three = Node(3)

    linkedList = LinkedList()
    linkedList.insertLast(one)
    linkedList.insertLast(two)
    linkedList.insertLast(three)

    iterator = LinkedListIterator(linkedList)
    assert iterator.next() == one
    assert iterator.hasNext() == True
    assert iterator.next() == two
    assert iterator.next() == three
    assert iterator.hasNext() == False

    # iterator2 = LinkedListIterator(linkedList)

    # while iterator2.hasNext():
    #     print("Item : ", iterator2.next())


def testInsertFirstEmptyCase():
    first = Node(10)
    linkedList = LinkedList()
    linkedList.insertFirst(first)

    iterator = LinkedListIterator(linkedList)

    assert iterator.next() == first


def testInsertFirstManyCase():
    first = Node(10)
    second = Node(20)
    third = Node(30)
    linkedList = LinkedList()
    linkedList.insertFirst(first)
    linkedList.insertFirst(second)
    linkedList.insertFirst(third)

    iterator = LinkedListIterator(linkedList)

    assert iterator.next() == third
    assert iterator.next() == second
    assert iterator.next() == first


def testInsertFirstAndLastManyCase():
    first = Node(10)
    second = Node(20)
    third = Node(30)
    fourth = Node(40)
    linkedList = LinkedList()
    linkedList.insertFirst(first)
    linkedList.insertFirst(second)
    linkedList.insertLast(third)
    linkedList.insertLast(fourth)

    iterator = LinkedListIterator(linkedList)

    assert iterator.next() == second
    assert iterator.next() == first
    assert iterator.next() == third
    assert iterator.next() == fourth


def testDeleteFirst():
    first = Node(10)
    linkedList = LinkedList()
    linkedList.insertFirst(first)

    linkedList.deleteFirst()
    assert linkedList.isEmpty() == True


def testDeleteFirstMany():
    first = Node(10)
    second = Node(20)
    linkedList = LinkedList()
    linkedList.insertFirst(first)
    linkedList.insertFirst(second)

    linkedList.deleteFirst()

    iterator = LinkedListIterator(linkedList)
    assert iterator.next() == first
    assert iterator.hasNext() == False


def testDeleteNodeFirst():
    first = Node(10)
    second = Node(20)
    linkedList = LinkedList()
    linkedList.insertFirst(first)
    linkedList.insertLast(second)

    linkedList.delete(first)

    iterator = LinkedListIterator(linkedList)
    assert iterator.next() == second
    assert iterator.hasNext() == False



def testDeleteNodeFirst():
    first = Node(10)
    second = Node(20)
    linkedList = LinkedList()
    linkedList.insertFirst(first)
    linkedList.insertLast(second)

    linkedList.delete(second)

    iterator = LinkedListIterator(linkedList)
    assert iterator.next() == first
    assert iterator.hasNext() == False


def testDeleteNodeMany():
    first = Node(10)
    second = Node(20)
    third = Node(30)
    fourth = Node(40)
    linkedList = LinkedList()
    linkedList.insertFirst(first)
    linkedList.insertLast(second)
    linkedList.insertLast(third)
    linkedList.insertLast(fourth)

    linkedList.delete(third)

    iterator = LinkedListIterator(linkedList)
    assert iterator.next() == first
    assert iterator.next() == second
    assert iterator.next() == fourth
    assert iterator.hasNext() == False
