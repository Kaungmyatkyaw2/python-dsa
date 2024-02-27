class InsertionSort:
    def sort(self, items):
        for i in range(1,len(items)):
            j = i
            while j > 0 and items[j-1] > items[j]:
                [items[j-1],items[j]] = [items[j],items[j-1]]
                j -= 1 

        return items
