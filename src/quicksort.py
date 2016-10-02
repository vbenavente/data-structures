""" This module is an implementation of the Hoare Quicksort algorithm.
This algorithm was derived from code found on the wikipedia page and the
interactive python page.

https://en.wikipedia.org/wiki/Quicksort
interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
"""


def qs(list_to_sort, low=None, high=None):
    """
    This implementation of Hoare's Partitioning Scheme uses two picot points
    which start at either end of the provided list and move towards each other
    until an inversion is detected. Those elements causing the inversion are
    then swapped. When the indicies meet, the algorithm stops and returns the
    final index
    """

    low = list_to_sort[0]
    high = list_to_sort[-1]

    if low < high:
        q = part(list_to_sort, low, high)
        qs(list_to_sort, low, q)
        qs(list_to_sort, q + 1, high)

    return list_to_sort


def part(list_to_sort, low=None, high=None):
    pivot = list_to_sort[low]
    start = low - 1
    end = high + 1
    processing = True
    while processing:
        while list_to_sort[start] < pivot:
            start = start + 1
        while list_to_sort[end] > pivot:
            end = end - 1
        if start >= end:
            return end
    list_to_sort[start], list_to_sort[end] = list_to_sort[end], list_to_sort[start]
