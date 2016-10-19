# -*- coding: utf-8 -*-
from radix_sort import radix_sort

BEST_CASE = [x for x in range(0, 100)]
WORST_CASE = BEST_CASE[::-1]


def test_radix_sort():
    """Test radix sort sorts any list passed in."""
    result = radix_sort([5, 30, 20, 3, 17, 11, 2, 6, 35])
    assert result == sorted([5, 30, 20, 3, 17, 11, 2, 6, 35])


def test_radix_sort_empty_list():
    """Test radix sort returns empty list if passed empty list."""
    result = radix_sort([])
    assert result == []


def test_radix_sort_one_item_in_list():
    """Test radix sort works for one item in list."""
    result = radix_sort([5])
    assert result == [5]


def test_radix_sort_two_items_in_list():
    """Test radix sort works for two item list."""
    result = radix_sort([12, 7])
    assert result == sorted([12, 7])


def test_radix_sort_duplicates():
    """Test radix sort can handle large duplicate values."""
    duplicate_list = [7, 3, 6, 8, 4, 5, 10, 7]
    result = radix_sort(duplicate_list)
    assert result == sorted(duplicate_list)


def test_radix_sort_all_duplicates():
    """Test sort can handle a list of all duplicates."""
    result = radix_sort([3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
    assert result == sorted([3, 3, 3, 3, 3, 3, 3, 3, 3, 3])


def test_radix_sort_already_sorted():
    """Test sort returns sorted list if already sorted."""
    result = radix_sort(BEST_CASE)
    assert result == BEST_CASE


def test_radix_sort_reverse_sort_passed():
    """Test sort works when passed list is reversed."""
    result = radix_sort(WORST_CASE)
    assert result == sorted(WORST_CASE)
