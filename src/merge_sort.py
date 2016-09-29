# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import timeit

BEST_CASE = [x for x in range(0, 1000)]
WORST_CASE = BEST_CASE[::-1]


def merge_sort(a_list):
    """Use merge sort to sort the list."""
    if len(a_list) <= 1:
        return a_list
    left = []
    right = []
    for i in range(len(a_list)):
        if i % 2 != 0:
            left.append(a_list[i])
        else:
            right.append(a_list[i])
    left = merge_sort(left)
    right = merge_sort(right)
    return _merge(left, right)


def _merge(left, right):
    """Takes two lists and returns single sorted list."""
    new_list = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            new_list.append(left[left_idx])
            left_idx += 1
        else:
            new_list.append(right[right_idx])
            right_idx += 1
    while left_idx < len(left):
        new_list.extend([left[left_idx]])
        left_idx += 1
    while right_idx < len(right):
        new_list.extend([right[right_idx]])
        right_idx += 1
    return new_list


if __name__ == '__main__':
    print("Best Case: a list already in order")
    print("number of runs: 1000 / average time: " + str((timeit.Timer(
        "merge_sort(BEST_CASE)", setup="from __main__ import merge_sort, BEST_CASE").timeit(
            number=1000))/1000))
    print("Worst Case: a list in reverse order")
    print("number of runs: 1000 / average time: " + str(
        (timeit.Timer(
            "merge_sort(WORST_CASE)", setup="from __main__ import merge_sort, WORST_CASE").timeit(
                number=1000))/1000))
