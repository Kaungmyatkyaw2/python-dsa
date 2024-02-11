class BinarySearch:
    def __init__(self, items):
        self.items = items

    def search(self, item):
        first = 0
        last = len(self.items) - 1

        while first <= last:
            middle = int((first + last) / 2)
            middleElement = self.items[middle]
            if middleElement == item:
                return middle
            elif middleElement > item:
                last = middle - 1
            else:
                first = middle + 1
        return -1
