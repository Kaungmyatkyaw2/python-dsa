class DoublyLinkedList:
    def __init__(self):
        self.__first = None
        self.__last = None

    def isEmpty(self):
        return self.__first == None

    def insertFirst(self, node):
        if self.isEmpty():
            self.__first = node
            self.__last = node
        else:
            node.next = self.__first
            self.__first.previous = node
            self.__first = node

    def insertLast(self, node):
        if self.isEmpty():
            self.__first = node
            self.__last = node
        else:
            self.__last.next = node
            node.previous = self.__last
            self.__last = node

    def insertAfter(self, existingNode, newNode):
        if existingNode == self.__last:
            self.insertLast(newNode)
        else:
            newNode.next = existingNode.next
            newNode.previous = existingNode
            existingNode.next.previous = newNode
            existingNode.next = newNode

    def getFirst(self):
        return self.__first

    def getLast(self):
        return self.__last
