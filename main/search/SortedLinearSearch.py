class SortedLinearSearch:
    def __init__(self, items):
        self.items = items

    def search(self, item):
        n = len(self.items)
        index = 0

        while index < n and self.items[index] < item:
            index += 1

        if index >= n or self.items[index] != item:
            index = -1

        return index
