# -*- coding: utf-8 -*-
"""Docstring."""
import linked_list


class Stack(object):
    """Summary.

    Args:
        object (TYPE): Description

    Returns:
        TYPE: Description
    """

    def __init__(self, iterable=None):
        """Summary."""
        self.ll = linked_list.LinkedList(iterable)

    def push(self, value):
        """Summary.

        Returns:
            TYPE: Description
        """
        return self.ll.push(value)

    def pop(self):
        """Summary.

        Returns:
            TYPE: Description
        """
        return self.ll.pop()
