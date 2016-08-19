# -*- coding: utf-8 -*-
"""File tests doubly linked list functionality."""
from __future__ import unicode_literals
from dll import DoublyLinkedList
import pytest


TEST_DLL_PUSH = [
    ("hightower", "hightower"),
    ([1, 2, 3, 4], [1, 2, 3, 4])
]


def test_dll_init(dll_initial_1):
    assert dll_initial_1.head.data == [1, 2, 3]


def test_dll_init_error():
    with pytest.raises(TypeError):
        DoublyLinkedList(7)


@pytest.mark.parametrize("value, output", TEST_DLL_PUSH)
def test_dll_push(value, output, dll_initial_2):
    dll_initial_2.push(value)
    assert dll_initial_2.head.data == output


@pytest.mark.parametrize("value, output", TEST_DLL_PUSH)
def test_dll_append(value, output, dll_initial_2):
    dll_initial_2.append(value)
    assert dll_initial_2.tail.data == output


def test_dll_pop(dll_initial_2):
    assert dll_initial_2.pop() == [1, 99, 7]


def test_dll_shift(dll_initial_2):
    assert dll_initial_2.shift() == "booksarecool"
