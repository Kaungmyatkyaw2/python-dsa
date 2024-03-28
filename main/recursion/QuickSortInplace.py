class QuickSortInplace:

    def sort(self, items):
        return self.quickSort(items, 0, len(items) - 1)

    def quickSort(self, items, startIndex, endIndex):
        size = endIndex - startIndex + 1
        if size >= 3:

            left = startIndex
            right = endIndex
            pivot = items[endIndex]

            while left <= right:
                while items[left] < pivot:
                    left += 1

                while items[right] > pivot:
                    right -= 1

                if left <= right:
                    [items[left], items[right]] = [items[right], items[left]]
                    left += 1
                    right -= 1
            self.quickSort(items, startIndex, right)
            self.quickSort(items, left, endIndex)

        else:
            if size == 2:
                if items[startIndex] > items[endIndex]:
                    [items[startIndex], items[endIndex]] = [
                        items[endIndex],
                        items[startIndex],
                    ]
