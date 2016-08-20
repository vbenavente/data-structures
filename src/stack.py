# -*- coding: utf-8 -*-
"""File implements a basic stack data structure."""
import linked_list


class Stack(object):
    """Building our stack class."""

    def __init__(self, iterable=None):
        self.ll = linked_list.LinkedList(iterable)

    def push(self, value):
        """Adds a node with a value to the stack."""
        self.ll.push(value)

    def pop(self):
        """Removes a value from the stack and returns it."""
        return self.ll.pop()
