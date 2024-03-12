class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, node):
        if self.first == None:
            self.first = node

        if self.last != None:
            self.last.next = node
        self.last = node

    def showAll(self):
        currentNode = self.first

        while currentNode != None:
            print("Item ", currentNode.value)
            currentNode = currentNode.next


class LinkedListIterator:
    def __init__(self, list):
        self.currentNode = list.first

    def hasNext(self):
        return self.currentNode != None and self.currentNode.next != None

    def next(self):
        if self.currentNode != None:
            temp = self.currentNode
            self.currentNode = self.currentNode.next
            return temp.value

        return None
