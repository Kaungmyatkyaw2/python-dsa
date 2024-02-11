import pytest
from main.search.LinearSearch import LinearSearch
from main.search.SortedLinearSearch import SortedLinearSearch


def test_linearSearchWorstCase():
    array = LinearSearch([2, 3, 1, 10, 4, 5, 6, 7])
    assert array.search(50) == -1


def test_linearSearchAverageCase():
    array = LinearSearch([2, 3, 1, 10, 4, 5, 6, 7])
    assert array.search(10) == 3


def test_linearSEarchBestCase():
    array = LinearSearch([2, 3, 1, 10, 4, 5, 6, 7])
    assert array.search(2) == 0


def test_sortedLinearSearchWorstCase():
    array = SortedLinearSearch([1, 2, 3, 4, 5, 6])
    assert array.search(50) == -1


def test_sortedLinearSearchAverageCase():
    array = SortedLinearSearch([1, 2, 3, 4, 5, 6])
    assert array.search(3) == 2


def test_sortedLinearSearchBestCase():
    array = SortedLinearSearch([1, 2, 3, 4, 5, 6])
    assert array.search(1) == 0
