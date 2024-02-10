class LinearSearch:
    def __init__(self, items):
        self.items = items

    def findItem(self, item):
        n = len(self.items)

        for i in range(0, n):
            if self.items[i] == item:
                return i
                break
        return -1
