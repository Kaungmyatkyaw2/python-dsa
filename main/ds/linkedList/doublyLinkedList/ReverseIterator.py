class ReverseIterator:
    def __init__(self, list):
        self.currentNode = list.getLast()

    def hasNext(self):
        return self.currentNode != None  # and self.currentNode.next != None

    def next(self):
        if self.currentNode != None:
            temp = self.currentNode
            self.currentNode = self.currentNode.previous
            return temp

        return None
