import pytest
from main.recursion.MergeSort import sort
from main.util import isSorted,getRandomArray


def test_MergeSortBaseCase():
    arr = [6, 3]
    sort(arr)
    assert isSorted(arr) == True


def test_MergeSortManyElement():
    arr = [8,3,5,-8,1]
    sort(arr)
    assert isSorted(arr) == True

def test_MergedSortRandomArray():
    arr = getRandomArray(10,100)
    sort(arr)
    assert isSorted(arr) == True
