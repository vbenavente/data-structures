# -*- coding: utf-8 -*-
"""File implements a simple min-heap data structure in python."""
from __future__ import unicode_literals


class Heap(object):
    """Class implements a simple binary min-heap data structure in Python."""

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
        """Calls _push_onto and _sort_push methods in one function.

        This abstracts some of our functionality out into sub functions
        that are more easily testable.
        """
        self._push_onto(data)
        self.sort_push()

    def _push_onto(self, data):
        """Adds value into the heap without any sorting."""
        self.heap.append(data)

    def sort_push(self):
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

    def pop(self):
        """Removes value from heap, maintaining shape and heap properties."""
        # should return the value popped
        try:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        except IndexError:
            raise IndexError("You're a dumbass you can't pop an empty heap.")
        tail = self.heap[-1]
        return tail

    def _pop_from(self):
        pass
