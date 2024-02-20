import pytest
from main.sort.SelectionSort import SelectionSort
from main.util import isSorted, getRandomArray


def test_isSorted():
    assert isSorted([1, 2, 3, 4, 5]) == True
    assert isSorted([]) == True
    assert isSorted([1, 234, 3, 4, 5]) == False


def test_selectionSort():
    items = getRandomArray(10, 100)
    print("\nItems ", items)
    algo = SelectionSort()
    sortedItems = algo.sortInForLoop(items)
    print("Sorted Items ", sortedItems)
    assert isSorted(sortedItems) == True
