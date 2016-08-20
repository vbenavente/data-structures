# -*- coding: utf-8 -*-
"""File tests Stack module functionality."""
import pytest
from stack import Stack

TEST_INIT_DATA = [
    ("encyclopedia", "a"),
    ([4, 5, 6], 6)
]
TEST_PUSH_DATA = [
    ("dictionary", "y", "y"),
    ("bigandsmall", "word", "word")
]
TEST_POP_DATA = [
    ("dictionary", "y"),
    ("bigandsmall", "l")
]


@pytest.mark.parametrize("initial, result", TEST_INIT_DATA)
def test_stack_init(initial, result):
    """Function tests Stack init method."""
    test_case = Stack(initial)
    assert test_case.ll.head.data == result


@pytest.mark.parametrize("initial, value, result", TEST_PUSH_DATA)
def test_stack_push(initial, value, result):
    """Function tests Stack push method."""
    test_case = Stack(initial)
    test_case.push(value)
    assert test_case.ll.head.data == result


@pytest.mark.parametrize("initial, result", TEST_POP_DATA)
def test_stack_pop(initial, result):
    """Function tests Stack pop method."""
    test_case = Stack(initial)
    assert test_case.pop().data == result
    #this test fails, we'll fix it in our stack branch
