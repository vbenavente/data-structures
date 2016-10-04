# -*- coding: utf-8 -*-
"""File implements a priority queue data structure in python."""
from __future__ import unicode_literals
from heap import Heap


class Priorityq(object):
    """Class implements a priority queue data structure in Python."""
    order = 0

    def __init__(self, iterable=None):
        """Init instance of priority queue class,
        iterate through data if provided as an argument."""
        pq_list = []
        if iterable is None:
            self.heap = Heap()
        else:
            if not isinstance(iterable, list):
                raise IndexError("Enter a list of tuples, each with 2 values.")
            for i in iterable:
                if not isinstance(i, tuple):
                    raise IndexError("Enter a list of tuples, each with 2 values.")
                elif not isinstance(i[0], int):
                    raise IndexError("First value in tuple must be an integer.")
                self.order += 1
                new_tuple = (i[0], self.order, i[1])
                (pq_list).append(new_tuple)
        self.heap = Heap(pq_list)

    def insert(self, tup):
        """Inserts an item into the priority queue."""
        if not isinstance(tup, tuple):
            raise IndexError("Enter a tuple with 2 values.")
        elif not isinstance(tup[0], int):
            raise TypeError("First value in tuple must be an integer.")
        self.order += 1
        new_tuple = (tup[0], self.order, tup[1])
        self.heap.push(new_tuple)

    def pop(self):
        """Removes the most important item from the queue."""
        return self.heap.pop()[2]

    def peek(self):
        """Returns the most important item without
        removing it from the queue."""
        try:
            return self.heap.heap[0]
        except IndexError:
            raise IndexError("You can't peek at an empty priority queue.")
