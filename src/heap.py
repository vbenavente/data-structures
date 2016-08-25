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
        # should return the value popped
        pass

    def _swap(self):
        """Swaps the values of two list indexes."""
        pass

    def sort_parent(self):
        """Uses math to find our index's parent value."""
        c_idx = len(self.heap) - 1
        c_val = self.heap[c_idx]
        p_idx = (c_idx - 1) // 2
        p_val = self.heap[p_idx]
        while p_val > c_val:
            self.heap[p_idx], self.heap[c_idx] = self.heap[c_idx], self.heap[p_idx]
            c_idx = p_idx
            p_idx = (p_idx - 1) // 2
            p_val = self.heap[p_idx]
            c_val = self.heap[c_idx]
            if p_val < c_val:
                break
