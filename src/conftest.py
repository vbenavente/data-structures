# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest


"""DLL Fixtures"""

TEST_DLL_INIT_DATA = [
    ("encyclopedia",),
    "taco",
    "zebra",
    [1, 2, 3],
]

TEST_DLL_INIT_DATA2 = [
    ("booksarecool",),
    "rhino",
    [1, 99, 7],
]


@pytest.fixture(scope="function")
def dll_initial_1():
    from dll import DoublyLinkedList
    temp = DoublyLinkedList(TEST_DLL_INIT_DATA)
    return temp


@pytest.fixture(scope="function")
def dll_initial_2():
    from dll import DoublyLinkedList
    temp = DoublyLinkedList(TEST_DLL_INIT_DATA2)
    return temp


"""Heap Fixtures"""

HEAP_FIX_ONE_DATA = [
    (1, ),
    (1, 2),
    (2, 1),
    (45, 87, 3, 27),
    (7, 5, 9, 345, 43, 873),
    (8, 7, 6, 5, 4, 3, 2, 1),
    (1, 2, 3, 4, 5, 6, 7, 8, 9),
    (34, 0, 77, 95, 21, 8009, 788324),
    range(700)
]


@pytest.fixture(scope="function")
def heap_fix_empty():
    """Return a new test instance of Heap class."""
    from heap import Heap
    instance = Heap()
    return instance


@pytest.fixture(scope="function", params=HEAP_FIX_ONE_DATA)
def heap_fix_one(request):
    """Return a new test instance of Heap class."""
    from heap import Heap
    instance = Heap(request.param)
    expected = sorted(request.param)[0]
    return instance, expected
