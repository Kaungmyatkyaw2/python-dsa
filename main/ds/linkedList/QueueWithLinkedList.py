from main.ds.linkedList.LinkedList import LinkedList
from main.ds.linkedList.Node import Node
from main.ds.queue.Queue import QueueOverflowException


class QueueWithLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def enque(self, value):
        node = Node(value)
        self.insertLast(node)

    def deque(self):
        first = self.getFirst()
        if first == None:
            raise QueueOverflowException("Queue is empty.")
        else:
            self.deleteFirst()
            return first.value
