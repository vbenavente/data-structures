#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import timeit


BEST_CASE = [x for x in range(0, 1000)]
WORST_CASE = BEST_CASE[::-1]


def quick_sort(a_list):
    """Use quick sort to sort the list."""
    left = []
    right = []
    if len(a_list) <= 1:
        return a_list
    if len(a_list) == 2:
        if a_list[0] < a_list[1]:
            left.append(a_list[0])
            right.append(a_list[1])
        else:
            left.append(a_list[1])
            right.append(a_list[0])
    else:
        hi = a_list[-1]
        low = a_list[0]
        midpoint = a_list[len(a_list)//2]
        pivot = sorted([low, hi, midpoint])[1]
        for item in a_list:
            if item < pivot:
                left.append(item)
            else:
                right.append(item)
    left = quick_sort(left)
    right = quick_sort(right)
    return left + right


if __name__ == '__main__':
    print("Best Case: a list already in order")
    print("number of runs: 1000 / average time: " + str((timeit.Timer(
        "quick_sort(BEST_CASE)", setup="from __main__ import quick_sort, BEST_CASE").timeit(
            number=1000))/1000))
    print("Worst Case: a list in reverse order")
    print("number of runs: 1000 / average time: " + str(
        (timeit.Timer(
            "quick_sort(WORST_CASE)", setup="from __main__ import quick_sort, WORST_CASE").timeit(
                number=1000)/1000)))
