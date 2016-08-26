# -*- coding: utf-8 -*-
"""File tests our heap data structure implementation."""
from __future__ import unicode_literals
# import pytest


def test_heap_init_empty(heap_fix_empty):
    """Test the init method with no data passed in."""
    assert heap_fix_empty.heap == []


def test_heap_init(heap_fix_one):
    """Ensure that the init method of Heap class works correctly."""
    assert heap_fix_one.instance.heap[0] == heap_fix_one.result


def test_heap_push_onto_empty(heap_fix_empty):
    """Test push onto an empty Heap."""
    heap_fix_empty._push_onto(63)
    assert heap_fix_empty.heap[-1] == 63


def test_heap_push_onto(heap_fix_one):
    """Ensure that the push method adds a value to binary heap."""
    heap_fix_one.instance._push_onto(63)
    assert heap_fix_one.instance.heap[-1] == 63


def test_heap_pop_empty():
    """Test pop from an empty list returns None."""
    pass


def test_heap_pop():
    """Ensure that the pop method removes a value from binary heap."""
    pass


def test_heap_swap():
    """Swaps the values of two list indexes."""
    pass


def test_heap_push(heap_fix_one):
    """Uses math to find our index's parent value."""
    # instance = heap_fix_one[0]
    heap_fix_one.instance.push(63)
    print('after', heap_fix_one.instance.heap.index(63))
    assert (heap_fix_one.instance.heap).index(63) == heap_fix_one.expected
