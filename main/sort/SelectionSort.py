class SelectionSort:

    def sort(self, items):
        i = 0
        while i < len(items) - 1:
            j = i + 1
            minIndex = i
            while j < len(items):
                if items[minIndex] > items[j]:
                    minIndex = j
                j += 1
            [items[i], items[minIndex]] = [
                items[minIndex],
                items[i],
            ]
            i += 1
        return items

    def sortInForLoop(self, items):
        for i in range(0,len(items) - 1):
            minIndex = i
            for j in range(i + 1, len(items)):
                if items[minIndex] > items[j]:
                    minIndex = j
            [items[i], items[minIndex]] = [items[minIndex], items[i]]

        return items
