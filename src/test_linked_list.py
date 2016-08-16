# -*- coding: utf-8 -*-
"""Summary."""
import pytest
# from linked_list import Node
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


@pytest.mark.parametrize("data, output", TEST_LINKED_LIST_INIT_DATA)
def test_linked_list_init(data, output):
    """Summary.

    Returns:
        TYPE: Description
    """
    test_case = LinkedList(data)
    assert test_case.head.data == output


@pytest.mark.parametrize("data, data2, output", TEST_PUSH_DATA)
def test_push(data, data2, output):
    """Test the push method of LinkedList class."""
    test_case = LinkedList(data)
    test_case.push(data2)
    assert test_case.head.data == output
