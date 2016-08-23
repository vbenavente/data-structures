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


def test_deque_append_one():
    """Test that append method adds specified data to the deque."""
    test_case = Deque(TEST_DEQUE_INIT_DATA)
    original_size = test_case.size()
    test_case.append("string")
    assert test_case.dll.head.data == "string"
    assert test_case.size() == original_size + 1


def test_deque_append_several():
    """Test that the append method adds specified data to the deque."""
    test_case = Deque(TEST_DEQUE_INIT_DATA)
    test_case.append("one")
    test_case.append("two")
    test_case.append("three")
    assert test_case.dll.head.data == "three"
    assert test_case.size() == 8


def test_deque_append_empty():
    """Test that the append method properly hooks up the tail when you
    add to an empty list."""
    test_case = Deque()
    test_case.append("a value")
    assert test_case.dll.head.data == "a value"
    assert test_case.dll.tail.data == "a value"
    assert test_case.size() == 1


def test_deque_appendleft_one():
    """Test that appendleft method adds specified data to the deque."""
    test_case = Deque(TEST_DEQUE_INIT_DATA)
    original_size = test_case.size()
    test_case.appendleft("string")
    assert test_case.dll.tail.data == "string"
    assert test_case.size() == original_size + 1


def test_deque_appendleft_several():
    """Test that appendleft method adds specified data to the deque."""
    test_case = Deque(TEST_DEQUE_INIT_DATA)
    test_case.appendleft("one")
    test_case.appendleft("two")
    test_case.appendleft("three")
    assert test_case.dll.tail.data == "three"
    assert test_case.size() == 8


def test_deque_appendleft_empty():
    """Test that appendleft method properly hooks up the head when you
    add to an empty list."""
    test_case = Deque()
    test_case.appendleft("a value")
    assert test_case.dll.head.data == "a value"
    assert test_case.dll.tail.data == "a value"
    assert test_case.size() == 1


def test_deque_pop():
    """Test pop removes a value from the head(end) of the deque."""
    test_case = Deque(TEST_DEQUE_INIT_DATA)
    plop = test_case.pop()
    assert plop == ("cup", "coffee", "pastry")
    assert test_case.size() == 4


def test_deque_pop_empty():
    """Test pop from empty deque raises appropriate error."""
    test_case = Deque()
    with pytest.raises(IndexError) as message:
        test_case.pop()
    assert "The deque is empty." in str(message)


def test_deque_pop_from_one():
    """Test pop from deque with only one node."""
    test_case = Deque("e")
    assert test_case.pop() == "e"
    assert test_case.size() == 0


def test_deque_popleft():
    """Test popleft removes a value from the tail(front) of the deque."""
    test_case = Deque(TEST_DEQUE_INIT_DATA)
    print(test_case.size())
    plop = test_case.popleft()
    print(test_case.size())
    import pdb; pdb.set_trace()
    assert plop == [1, 2, 3, 4, 5]
    assert test_case.size() == 4


def test_deque_popleft_empty():
    """Test popleft from empty deque raises appropriate error."""
    test_case = Deque()
    with pytest.raises(IndexError) as message:
        test_case.popleft()
    assert "The deque is empty." in str(message)


def test_deque_popleft_from_one():
    """Test popleft from deque with only one node."""
    test_case = Deque("e")
    assert test_case.popleft() == "e"
    assert test_case.size() == 0
