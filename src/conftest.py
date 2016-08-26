# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import namedtuple
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

Heap_Fix = namedtuple("Heap_Fix", ("data",
                                   "result",
                                   "output",
                                   "input",
                                   "instance",
                                   "expected",
                                   ))
Heap_Fix.__new__.__defaults__ = (None,) * len(Heap_Fix._fields)
# the above line sourced from:
# http://stackoverflow.com/questions/11351032/named-tuple-and-optional-keyword-arguments

HEAP_FIX_ONE_DATA = [
    ((1, ), (1)),
    ((1, 2), (2)),
    ((2, 1), (2)),
    ((45, 87, 3, 27), (4)),
    ((7, 5, 9, 345, 43, 873), (6)),
    ((8, 7, 6, 5, 4, 3, 2, 1), (8)),
    ((1, 2, 3, 4, 5, 6, 7, 8, 9), (9)),
    ((34, 0, 77, 95, 21, 8009, 788324), (3)),
    (list(range(64, 200)), (0)),
    (list(range(-15, 50)), (65))
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
    instance = Heap(request.param[0])
    result = sorted(request.param[0])[0]
    expected = request.param[1]
    named_tuple = Heap_Fix(instance=instance, result=result, expected=expected)
    return named_tuple
