import pytest
from main.sort.InsertionSort import InsertionSort
from main.util import isSorted


def test_insertionSort():
    items = [5, 3, 7, 6, 11, 1]
    algo = InsertionSort()
    print("\nUnSorted Items : ", items)
    algo.sort(items)
    print("Sorted Items   : ", items)
    assert isSorted(items) == True
