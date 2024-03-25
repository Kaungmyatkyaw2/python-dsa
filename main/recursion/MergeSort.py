def sort(arr):
    mergeSort(arr, 0, len(arr) - 1)


def mergeSort(arr, startIndex, endIndex):
    if startIndex < endIndex:
        middle = int((startIndex + endIndex) / 2)
        size = (endIndex - startIndex) + 1

        if size > 2:
            mergeSort(arr, startIndex, middle)
            mergeSort(arr, middle + 1, endIndex)

        i = startIndex #3
        j = middle + 1 #4

        tempArr = [0] * size
        curIndex = 0

        while i <= middle and j <= endIndex:
            if arr[i] < arr[j]:
                tempArr[curIndex] = arr[i]
                i += 1
            else:
                tempArr[curIndex] = arr[j]
                j += 1

            curIndex += 1

        while i <= middle:
            tempArr[curIndex] = arr[i]
            i += 1
            curIndex += 1

        while j <= endIndex:
            tempArr[curIndex] = arr[j]
            j += 1
            curIndex += 1

        curIndex = 0

        print("Temp Arr :",tempArr,size,startIndex,endIndex)

        while startIndex <= endIndex:
            arr[startIndex] = tempArr[curIndex]
            startIndex += 1
            curIndex += 1
