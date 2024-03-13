from main.ds.linkedList.LinkedList import LinkedList
from main.ds.linkedList.Node import Node
from main.ds.stack.Stack import StackUnderflowException


class StackWithLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def push(self, value):
        node = Node(value)
        self.insertLast(node)

    def pop(self):
        last = self.getLast()
        if last == None:
            raise StackUnderflowException("Stack is empty.")
        else:
            self.delete(last)
            return last.value
