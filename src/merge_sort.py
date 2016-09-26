# -*- coding: utf-8 -*-
from __future__ import unicode_literals


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
    while left and right:
        if left[0] < right[0]:
            new_list.append(left[0])
            left = left[1:]
        else:
            new_list.append(right[0])
            right = right[1:]
    while left:
        new_list.append(left[0])
        left = left[1:]
    while right:
        new_list.append(right[0])
        right = right[1:]
    return new_list
