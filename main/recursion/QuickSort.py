class QuickSort:

    def sort(self, items):
        return self.quickSort(items, 0, len(items) - 1)

    def quickSort(self, items, startIndex, endIndex):
        size = endIndex - startIndex + 1
        if size >= 3:

            pivot = endIndex
            smallerEle = []
            graterEle = []

            curIndex = startIndex

            while curIndex <= endIndex-1:
                if items[curIndex] <= items[pivot]:
                    smallerEle.append(items[curIndex])
                else:
                    graterEle.append(items[curIndex])
                curIndex+=1

            curIndex = startIndex

            for i in smallerEle:
                items[curIndex] = i
                curIndex+=1

            items[curIndex] = items[pivot]
            pivotIndex = curIndex
            curIndex += 1

            for i in graterEle:
                items[curIndex] = i
                curIndex+=1

            self.quickSort(items,startIndex,pivotIndex-1)
            self.quickSort(items,pivotIndex+1,endIndex)
            
            

        else:
            if size == 2:
                if items[startIndex] > items[endIndex]:
                    [items[startIndex], items[endIndex]] = [
                        items[endIndex],
                        items[startIndex],
                    ]
