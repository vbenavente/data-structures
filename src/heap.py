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
            p_idx = (c_idx - 1) // 2
            p_val = self.heap[p_idx]
            c_val = self.heap[c_idx]
            if p_val < c_val or c_idx is 0:
                break

    def pop(self):
        """Removes value from heap, maintaining shape and heap properties."""
        try:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        except IndexError:
            raise IndexError("You're a silly head, we can't pop an empty heap.")
        tail = self.heap.pop()
        cur_idx = 0
        sort = True
        while sort:
            ch_a_idx, ch_b_idx = self._find_childs(cur_idx)
            min_ch_idx = self._min_child(ch_a_idx, ch_b_idx)
            if min_ch_idx is None:
                return tail
            if min_ch_idx > len(self.heap) - 1:
                sort = False
            if self.heap[cur_idx] > self.heap[min_ch_idx]:
                self.heap[cur_idx], self.heap[min_ch_idx] = self.heap[min_ch_idx], self.heap[cur_idx]
                cur_idx = min_ch_idx
            else:
                return tail

    def _min_child(self, ch_a_idx, ch_b_idx):
        """Returns index of min child.

        Returns None if index is past end of list."""
        ch_a_val = None
        ch_b_val = None
        try:
            ch_a_val = self.heap[ch_a_idx]
            ch_b_val = self.heap[ch_b_idx]
            if ch_a_val > ch_b_val:
                return ch_b_idx
            else:
                return ch_a_idx
        except TypeError:
            if ch_a_val is not None:
                return ch_a_idx
            else:
                return None

    def _find_childs(self, cur_idx):
        """Finds the index of children of a given index."""
        ch_a_idx = cur_idx * 2 + 1
        ch_b_idx = cur_idx * 2 + 2
        if ch_a_idx > len(self.heap) - 1:
            ch_a_idx = None
        if ch_b_idx > len(self.heap) - 1:
            ch_b_idx = None
        return ch_a_idx, ch_b_idx
