class BinarySearchRecursive:
    def __init__(self, items):
        self.items = items

    def search(self, item):
        first = 0
        last = len(self.items) - 1

        return self.findItem(item, first, last)

    def findItem(self, item, first, last):

        if first <= last:
            middle = int((first + last) / 2)
            if item < self.items[middle]:
                return self.findItem(item, first, middle - 1)
            elif item > self.items[middle]:
                return self.findItem(item, middle + 1, last)
            else:
                return middle
        else:
            return -1
