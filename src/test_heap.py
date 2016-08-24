# -*- coding: utf-8 -*-
"""File tests our heap data structure implementation."""
from __future__ import unicode_literals


def test_heap_init(heap_fix_one):
    from heap import Heap
    """Ensure that the init method of Heap class works correctly."""
    assert type(heap_fix_one) is Heap

# def test_heap_init_
