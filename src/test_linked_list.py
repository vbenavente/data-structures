# -*- coding: utf-8 -*-
"""File tests LinkedList functionality."""
from __future__ import unicode_literals
import pytest
from linked_list import LinkedList

TEST_LINKED_LIST_INIT_DATA = [
    ("frog", 'g'),
    (["one", "two", "three"], "three")
]
TEST_PUSH_DATA = [
    ("taco", "burrito", "burrito"),
    ("a", "b", "b"),
    ("cat", "dog", "dog"),
    ("z", [1, 2, 3], [1, 2, 3])
]
TEST_POP_DATA = [
    ("zebra", "a"),
    ("encyclopedia", "a"),
    ([1, 3, 5], 5)
]
TEST_SIZE_DATA = [
    ("taco", 4),
    ([1, 2, 3], 3)
]
TEST_SEARCH_DATA = [
    ("string", "i", "i"),
    ([1, 2, 7, 8], 8, 8)
]
TEST_REMOVE_DATA = [
    ("encyclopedia", "i", "i"),
    ("zebrasarecool", "b", "b"),
]
TEST_DISPLAY = [
    ("zebra", "(a, r, b, e, z)"),
    ([1, 2, 3], "(3, 2, 1)")
]


@pytest.mark.parametrize("data, output", TEST_LINKED_LIST_INIT_DATA)
def test_linked_list_init(data, output):
    """Test the __init__ of LinkedList class."""
    test_case = LinkedList(data)
    assert test_case.head.data == output


@pytest.mark.parametrize("data, data2, output", TEST_PUSH_DATA)
def test_push(data, data2, output):
    """Test the push method of LinkedList class."""
    test_case = LinkedList(data)
    test_case.push(data2)
    assert test_case.head.data == output


@pytest.mark.parametrize("data, output", TEST_POP_DATA)
def test_pop(data, output):
    """Test the pop method of LinkedList class."""
    test_case = LinkedList(data)
    assert test_case.pop().data == output


@pytest.mark.parametrize("data, output", TEST_SIZE_DATA)
def test_size(data, output):
    """Test the size method of LinkedList class."""
    test_case = LinkedList(data)
    assert test_case.size() == output


@pytest.mark.parametrize("data, output", TEST_SIZE_DATA)
def test_dunder_len(data, output):
    """Test the dunder len method of LinkedList class."""
    test_case = LinkedList(data)
    assert len(test_case) == output


@pytest.mark.parametrize("initial, query, output", TEST_SEARCH_DATA)
def test_search(initial, query, output):
    """Test the search method of LinkedList with test data."""
    test_case = LinkedList(initial)
    assert test_case.search(query).data == output


@pytest.mark.parametrize("initial, data, result", TEST_REMOVE_DATA)
def test_remove(initial, data, result):
    """Test the remove method of LinkedList class."""
    test_case = LinkedList(initial)
    test_case_node = test_case.search(data)
    assert test_case.remove(test_case_node).data == result


@pytest.mark.parametrize("initial, result", TEST_DISPLAY)
def test_display(initial, result):
    """Test the display method of LinkedList class."""
    test_case = LinkedList(initial)
    assert test_case.display() == result
