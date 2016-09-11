# -*- coding: utf-8 -*-
"""File tests our heap data structure implementation."""
from __future__ import unicode_literals
import pytest


def test_heap_init_empty(heap_fix_empty):
    """Test the init method with no data passed in."""
    assert heap_fix_empty.heap == []


def test_heap_init_non_iterable():
    """Tests that heap init w/ invalid value throws the appropriate error."""
    from heap import Heap
    with pytest.raises(TypeError) as message:
        Heap(1)
    assert "Please enter an object that is iterable." in str(message)


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


def test_heap_push(heap_fix_one):
    """Uses math to find our index's parent value."""
    heap_fix_one.instance.push(63)
    assert (heap_fix_one.instance.heap).index(63) == heap_fix_one.expected


def test_heap_pop_empty(heap_fix_empty):
    """Test pop from an empty list returns None."""
    with pytest.raises(IndexError) as message:
        heap_fix_empty.pop()
    assert "You're a silly head, we can't pop an empty heap." in str(message)


def test_heap_find_childs(heap_fix_one):
    """Ensure that find childs method returns childs index."""
    assert heap_fix_one.instance._find_childs(3) == heap_fix_one.childs


def test_heap_min_child():
    """Swaps the values of two list indexes."""
    from heap import Heap
    test_case = Heap([2, 4, 6, 9, 3, 5, 7])
    assert test_case._min_child(1, 2) == 1


def test_heap_pop(heap_fix_one):
    """Ensure that the pop method removes a value from binary heap."""
    catcher = []
    while len(heap_fix_one.instance.heap) > 0:
        (catcher).append(heap_fix_one.instance.pop())
    assert heap_fix_one.initial == catcher


def test_heap_push_pop(heap_fix_one, heap_fix_empty):
    """Ensue that after pushing we can successfully pop our heap."""
    catcher = []
    length = len(heap_fix_one.initial)
    while len(heap_fix_one.initial) > 0:
        heap_fix_empty.push(heap_fix_one.initial.pop())
    while len(heap_fix_empty.heap) > 0:
        (catcher).append(heap_fix_empty.pop())
    assert len(catcher) == length


def test_heap_pop_push(heap_fix_one):
    """Ensure that after popping we can successfully push."""
    heap_fix_one.instance.pop()
    heap_fix_one.instance.push(63)
    assert 63 in heap_fix_one.instance.heap
