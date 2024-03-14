class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous
