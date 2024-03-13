class LinkedList:
    def __init__(self):
        self.__first = None
        self.__last = None

    def insertLast(self, node):
        if self.__first == None:
            self.__first = node
            self.__last = node
            return

        self.__last.next = node
        self.__last = node

    def insertFirst(self, node):
        if self.__first == None:
            self.__first = node
            self.__last = node
            return

        node.next = self.__first
        self.__first = node

    def deleteFirst(self):
        if self.__first != None:
            self.__first = self.__first.next
            if self.__first == None:
                self.__last = None

    def delete(self, node):
        if not self.isEmpty():
            if node == self.__first:
                # self.deleteFirst() (or)
                self.__first = self.__first.next
                if self.__first == None:
                    self.__last = None
            else:
                previous = self.__first
                current = previous.next

                while current != None:
                    if current == node:
                        if current.next == None:
                            self.__last = previous
                        previous.next = current.next
                        node.next = None
                        break

                    previous = current
                    current = current.next

    def showAll(self):
        currentNode = self.__first

        while currentNode != None:
            print("Item ", currentNode.value)
            currentNode = currentNode.next

    def isEmpty(self):
        return self.__first == None

    def getLast(self):
        return self.__last

    def getFirst(self):
        return self.__first


class LinkedListIterator:
    def __init__(self, list):
        self.currentNode = list.getFirst()

    def hasNext(self):
        return self.currentNode != None  # and self.currentNode.next != None

    def next(self):
        if self.currentNode != None:
            temp = self.currentNode
            self.currentNode = self.currentNode.next
            return temp.value

        return None
