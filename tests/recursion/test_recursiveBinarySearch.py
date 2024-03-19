import pytest
from main.recursion.BinarySearchRecursive import BinarySearchRecursive


def test_BinarySearchRecursiveWorstCase():
    array = BinarySearchRecursive([1, 2, 3, 4, 5, 6])
    assert array.search(-7) == -1


def test_BinarySearchRecursiveAverageCaseLeftSide():
    array = BinarySearchRecursive([1, 2, 3, 4, 5, 6])
    assert array.search(3) == 2

def test_BinarySearchRecursiveAverageCaseRightSide():
    array = BinarySearchRecursive([1, 2, 3, 4, 5, 6])
    assert array.search(6) == 5


def test_BinarySearchRecursiveBestCase():
    array = BinarySearchRecursive([1, 2, 3, 4, 5, 6])
    assert array.search(1) == 0
