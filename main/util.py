import random


def isSorted(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True


def getRandomArray(size, _range):
    array = []
    for i in range(size):
        array.append(int(random.random() * _range))
    return array
