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
            # import pdb; pdb.set_trace()
            self.heap[p_idx], self.heap[c_idx] = self.heap[c_idx], self.heap[p_idx]
            c_idx = p_idx
            p_idx = (c_idx - 1) // 2
            p_val = self.heap[p_idx]
            c_val = self.heap[c_idx]
            if p_val < c_val or c_idx is 0:
                break

    def pop(self):
        """Removes value from heap, maintaining shape and heap properties."""
        # should return the value popped
        try:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        except IndexError:
            raise IndexError("You're a silly head, we can't pop an empty heap.")
        tail = self.heap.pop()
        cur_idx = 0
        ch_a_idx = 1
        ch_b_idx = 2
        cur_val = self.heap[0]
        ch_a_val = self.heap[1]
        ch_b_val = self.heap[2]
        truthy = True
        print(self.heap)
        while (cur_val > ch_a_val and ch_b_val) and truthy:
            if cur_val > ch_a_val:
                self.heap[cur_idx], self.heap[ch_a_idx] = self.heap[ch_a_idx], self.heap[cur_idx]
                cur_idx = ch_a_idx
            else:
                self.heap[cur_idx], self.heap[ch_b_idx] = self.heap[ch_b_idx], self.heap[cur_idx]
                cur_idx = ch_b_idx
            ch_a_idx = cur_idx * 2 + 1
            ch_b_idx = cur_idx * 2 + 2
            print("ch a idx before", ch_a_idx)
            print("ch b idx before", ch_b_idx)
            if ch_b_idx > len(self.heap) - 1:
                # print("hit if b")
                ch_b_idx = len(self.heap) - 1
                # truthy = False
                if cur_val > ch_b_val:
                    self.heap[cur_idx], self.heap[ch_b_idx] = self.heap[ch_b_idx], self.heap[cur_idx]
                return tail
            elif ch_a_idx > len(self.heap) - 1:
                # print("hit if a")
                ch_a_idx = len(self.heap) - 1
                # truthy = False
                if cur_val > ch_a_val:
                    self.heap[cur_idx], self.heap[ch_a_idx] = self.heap[ch_a_idx], self.heap[cur_idx]
                return tail
            print("ch a idx after", ch_a_idx)
            print("ch b idx after", ch_b_idx)
            print("1", self.heap)
            print("cur val", cur_val)
            print("cur idx", cur_idx)
            # import pdb; pdb.set_trace()
            ch_a_val = self.heap[ch_a_idx]
            ch_b_val = self.heap[ch_b_idx]
            cur_val = self.heap[cur_idx]
            print("2", self.heap)
            if cur_val < ch_a_val and ch_b_val:
                print("inside the if block")
                break
            print("3", self.heap)
            print("ch a val", ch_a_val)
            print("ch b val", ch_b_val)
        return tail

    def _pop_from(self):
        pass
