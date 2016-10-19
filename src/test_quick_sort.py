# -*- coding: utf-8 -*-
from quick_sort import quick_sort

BEST_CASE = [x for x in range(0, 100)]
WORST_CASE = BEST_CASE[::-1]


def test_quick_sort():
    """Test merge sort sorts any list passed in."""
    result = quick_sort([5, 30, 20, 3, 17, 11, 2, 6, 35])
    assert result == sorted([5, 30, 20, 3, 17, 11, 2, 6, 35])


def test_quick_sort_empty_list():
    """Test if empty list is passed, empty list is returned."""
    result = quick_sort([])
    assert result == []


def test_quick_sort_one_item():
    """Test one item in list returns list."""
    single_item_list = [5]
    result = quick_sort(single_item_list)
    assert result == single_item_list


def test_quick_sort_duplicates():
    """Test quick sort can handle duplicate values."""
    duplicate_list = [3, 6, 8, 4, 5, 10, 3]
    result = quick_sort(duplicate_list)
    assert result == sorted(duplicate_list)


def test_quick_sort_duplicates_large():
    """Test quick sort can handle large duplicate values."""
    duplicate_list = [7, 3, 6, 8, 4, 5, 10, 7]
    result = quick_sort(duplicate_list)
    assert result == sorted(duplicate_list)


def test_quick_sort_all_duplicates():
    """Test sort can handle a list of all duplicates."""
    result = quick_sort([3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
    assert result == sorted([3, 3, 3, 3, 3, 3, 3, 3, 3, 3])


def test_quick_sort_already_sorted():
    """Test sort returns sorted list if already sorted."""
    result = quick_sort(BEST_CASE)
    assert result == BEST_CASE


def test_quick_sort_reverse_sort_passed():
    """Test sort works when passed list is reversed."""
    result = quick_sort(WORST_CASE)
    assert result == sorted(WORST_CASE)
