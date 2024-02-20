import pytest
from main.sort.BubbleSort import BubbleSort
from main.util import isSorted, getRandomArray


def test_bubbleSort():
    items = getRandomArray(10, 100)
    print("\nItems ", items)
    algo = BubbleSort()
    sortedItems = algo.sort(items)
    print("Sorted Items ", sortedItems)
    assert isSorted(sortedItems) == True
