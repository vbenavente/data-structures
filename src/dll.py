# -*- coding: utf-8 -*-
"""Docstring."""


class Node(object):
    """Docstring."""
    def __init__(self, data=None, nxt=None, prev=None):
        """Docstring."""
        self.data = data
        self._next = nxt
        self._prev = prev


class DoublyLinkedList(object):
    """Docstring."""
    def __init__(self, iterable=None):
        """Docstring."""
        self.head = None
        self.tail = None
        try:
            if iterable:
                for item in iterable:
                    self.push(item)
        except TypeError:
            raise TypeError("Please enter an object that is iterable.")

    def push(self, data):
        """Docstring."""
        new_node = Node(data)
        new_node._prev = None
        new_node._next = self.head
        if self.head:
            self.head._prev = new_node._next
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def append(self, data):
        """Docstring."""
        new_node = Node(data)
        new_node._next = None
        new_node._prev = self.tail
        if self.tail:
            self.tail._next = new_node._prev
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def pop(self):
        """Docstring."""
        pop_node = self.head
        self.head._next._prev = None
        self.head = self.head._next
        return pop_node.data

    def shift(self):
        """Docstring."""
        shift_node = self.tail
        self.tail._prev._next = None
        self.tail = self.tail._prev
        return shift_node.data

    def remove(data):
        """Docstring."""
        pass
