import pytest
from main.recursion.QuickSortInplace import QuickSortInplace
from main.util import isSorted, getRandomArray


algo = QuickSortInplace()


def test_QuickSortBaseCase():
    arr = [6, 3]
    algo.sort(arr)
    assert isSorted(arr) == True


def test_QuickSortManyElement():
    arr = [8, 3, 5, -8, 1]
    algo.sort(arr)
    assert isSorted(arr) == True


def test_QuickSortRandomArray():
    arr = getRandomArray(10, 100)
    algo.sort(arr)
    assert isSorted(arr) == True
