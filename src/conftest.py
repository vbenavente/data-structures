# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

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
