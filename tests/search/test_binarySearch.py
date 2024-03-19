import pytest
from main.search.BinarySearch import BinarySearch


def test_BinarySearchWorstCase():
    array = BinarySearch([1, 2, 3, 4, 5, 6])
    assert array.search(-7) == -1


def test_BinarySearchAverageCaseLeftSide():
    array = BinarySearch([1, 2, 3, 4, 5, 6])
    assert array.search(3) == 2

def test_BinarySearchRecursiveAverageCaseRightSide():
    array = BinarySearch([1, 2, 3, 4, 5, 6])
    assert array.search(6) == 5

def test_BinarySearchBestCase():
    array = BinarySearch([1, 2, 3, 4, 5, 6])
    assert array.search(1) == 0
