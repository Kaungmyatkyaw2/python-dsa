import pytest
from main.ds.linkedList.LinkedList import LinkedList, LinkedListIterator
from main.ds.linkedList.Node import Node



def testShowAll():
    print("\n")
    one = Node(1)
    two = Node(2)
    three = Node(3)

    linkedList = LinkedList()
    linkedList.insert(one)
    linkedList.insert(two)
    linkedList.insert(three)
    # linkedList.showAll()

    # iterator = LinkedListIterator(linkedList)
    # assert iterator.next() == 1
    # assert iterator.hasNext() == True
    # assert iterator.next() == 2
    # assert iterator.hasNext() == False
    # assert iterator.next() == 3
    # assert iterator.hasNext() == False

    iterator = LinkedListIterator(linkedList)

    while iterator.hasNext():
        print("Item : ", iterator.next())
