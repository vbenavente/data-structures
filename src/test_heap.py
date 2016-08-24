# -*- coding: utf-8 -*-
"""File tests our heap data structure implementation."""
from __future__ import unicode_literals

A_CONSTANT = [
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
