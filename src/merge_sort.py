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
