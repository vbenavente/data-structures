# -*- coding: utf-8 -*-
"""File implements a simple heap data structure in python."""
from __future__ import unicode_literals


class Heap(object):
    """Class implements a simple binary heap data structure in Python."""

    def __init__(self, iterable=None):
        """Init method of Heap class, sets heap property as empty list."""
        if iterable is None:
            self.heap = []
            return
        try:
            self.heap = sorted(list(iterable))
        except TypeError:
            raise TypeError("Please enter an object that is iterable.")

    def push(self, data):
        """Adds value into the heap, maintaining shape and heap properties."""
        self.heap.append(data)

    def pop(self):
        """Removes value from heap, maintaining shape and heap properties."""
        pass

    def _swap(self):
        """Swaps the values of two list indexes."""
        pass

    def _find_parent(self):
        """Uses math to find our index's parent value."""
        pass

    def _find_children(self):
        """Uses math to find our value's children."""
        pass
