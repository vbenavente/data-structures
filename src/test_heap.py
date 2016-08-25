# -*- coding: utf-8 -*-
"""File tests our heap data structure implementation."""
from __future__ import unicode_literals
import pytest

HEAP_FIX_ONE_PARENT_DATA = [
    (63, 1),
    (63, 2),
    (63, 2),
    (63, 5),
    (63, 6),
    (63, 8),
    (63, 9),
    (63, 3),
    (63, 17),
]


def test_heap_init_empty(heap_fix_empty):
    """Test the init method with no data passed in."""
    assert heap_fix_empty.heap == []


def test_heap_init(heap_fix_one):
    """Ensure that the init method of Heap class works correctly."""
    heap, expected = heap_fix_one
    assert heap.heap[0] == expected


def test_heap_push_empty(heap_fix_empty):
    """Test push onto an empty Heap."""
    heap_fix_empty.push(63)
    assert heap_fix_empty.heap[0] == 63


def test_heap_push(heap_fix_one):
    """Ensure that the push method adds a value to binary heap."""
    heap_fix_one[0].push(63)
    assert heap_fix_one[0].heap[-1] == 63


def test_heap_pop_empty():
    """Test pop from an empty list returns None."""
    pass


def test_heap_pop():
    """Ensure that the pop method removes a value from binary heap."""
    pass


def test_heap_swap(self):
    """Swaps the values of two list indexes."""
    pass


@pytest.mark.parametrize("data, index", HEAP_FIX_ONE_PARENT_DATA)
def test_heap_sort_parent(data, index, heap_fix_one):
    """Uses math to find our index's parent value."""
    # instance = heap_fix_one[0]
    heap_fix_one[0].push(data)
    heap_fix_one[0].sort_parent()
    print('after', heap_fix_one[0].heap.index(data))
    assert (heap_fix_one[0].heap).index(data) == index
