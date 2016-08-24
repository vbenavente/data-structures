# -*- coding: utf-8 -*-
"""File implements a simple heap data structure in python."""
from __future__ import unicode_literals


class Heap(object):
    """Class implements a simple binary heap data structure in Python."""

    def __init__(self, iterable=None):
        heap_list = []
        try:
            for item in iterable:
                heap_list.append(item)
        except AttributeError:
            raise IndexError("Please enter an object that is iterable.")

    def push(self):
        """Adds value into the heap, maintaining shape and heap properties."""
        pass

    def pop(self):
        """Removes value from heap, maintaining shape and heap properties."""
        pass

    def _swap(self):
        """Swaps the values of two list indexes."""
        pass

    def _parse_list(self):
        """Decides how many levels our heap has and assigns blagh"""
        pass
