class BubbleSort:
    def sort(self,items):
        for i in range(len(items) - 1):
            for j in range(0, len(items) - (i + 1)):
                if items[j] > items[j + 1]:
                    [items[j], items[j + 1]] = [items[j + 1], items[j]]

        return items
