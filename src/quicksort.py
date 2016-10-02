""" This module is an implementation of the Hoare Quicksort algorithm.

This implementation of Hoare's Partitioning Scheme uses two picot points
which start at either end of the provided list and move towards each other
until an inversion is detected. Those elements causing the inversion are
then swapped. When the indicies meet, the algorithm stops and returns the
final index. This algorithm was derived from code found on the wikipedia page,
the interactive python page and pythonschool.net. Links below.


https://en.wikipedia.org/wiki/Quicksort
interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
pythonschool.net/data-structures-algorithms/quicksort
"""


def qs(list_to_sort):
    """This is the main function that the user calls with a list of numbers"""
    # import pdb; pdb.set_trace()
    if isinstance(list_to_sort, list):
        return qsh(list_to_sort, 0, len(list_to_sort) - 1)
    else:
        raise TypeError('Input type must be a list of integers')


def qsh(list_to_sort, low, high):
    """
    This helper function establishes the pivot point around which the list is
    sorted.
    """

    if low < high:
        q = part(list_to_sort, low, high)
        qsh(list_to_sort, low, q - 1)
        qsh(list_to_sort, q + 1, high)

    return list_to_sort


def part(list_to_sort, low, high):
    """
    This function rearranges the list by iterating over the list starting from
    the pivot provied until an inversion is detected.
    """

    pivot = list_to_sort[low]
    start = low + 1
    end = high
    processing = True
    while processing:
        while list_to_sort[start] <= pivot and start <= end:
            start += 1
        while list_to_sort[end] >= pivot and end >= start:
            end -= 1
        if end < start:
            processing = False
        else:
            list_to_sort[start], list_to_sort[end] = list_to_sort[end], list_to_sort[start]

    list_to_sort[low], list_to_sort[end] = list_to_sort[end], list_to_sort[low]

    return end
