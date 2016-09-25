# -*- coding: utf-8 -*-
"""The following code tests the insertion sort method implemented in
insertion_sort.py"""
from __future__ import unicode_literals
import random
import pytest


def test_insertion_sort_already_ordered():
    """Tests the insertion sort function with an already sorted sample."""
    test_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pass


def test_insertion_sort_worst_case():
    """Tests the insertion sort function with a worst case opposite ordered
    sample."""
    test_list_2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    pass


def test_insertion_sort_random_sample():
    """Tests the insertion sort method with a random sample."""
    test_list_3 = random.sample(range(1000), random.randrange(2, 500))
    pass


def test_insertion_sort_empty_list():
    """Tests that the insertion sort method raises approrpiate error if it's
    called on an empty list."""
    pass


def test_insertion_sort_not_list_error():
    """Tests that the insertion sort method throws an appropriate error if it's
    called on an object that isn't a valid python list."""
    pass
