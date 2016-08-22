# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
from deque import Deque

TEST_DEQUE_INIT_DATA = [
    [1, 2, 3, 4, 5],
    7,
    "zebra",
    {"whatup": "Vote For Pedro"},
    ("cup", "coffee", "pastry")
]

TEST_DEQUE_MUCHO_DATA = (("I love Zebras! ") * 200)


def test_deque_init():
    """Test that the deque initiliazed successfully."""
    test_case = Deque(TEST_DEQUE_INIT_DATA).dll
    assert test_case.head.data == ("cup", "coffee", "pastry")
    assert test_case.tail.data == [1, 2, 3, 4, 5]


def test_deque_init_empty():
    """Test that an empty deque's head and tail are None."""
    assert Deque().dll.head is None
    assert Deque().dll.tail is None


def test_deque_size():
    """Test the size method with a small, diverse initial list."""
    test_case = Deque(TEST_DEQUE_INIT_DATA)
    assert test_case.size() == 5


def test_deque_size_mucho():
    """Test the size method with a large initial list."""
    test_case = Deque(TEST_DEQUE_MUCHO_DATA)
    assert test_case.size() == 3000


def test_deque_size_empty():
    """Test the size method against an empty list."""
    test_case = Deque()
    assert test_case.size() == 0
