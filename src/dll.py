# -*- coding: utf-8 -*-
"""File implements a simple doubly linked list in python."""
from __future__ import unicode_literals


class Node(object):
    """Class implements Nodes for use in our dll."""
    def __init__(self, data=None, nxt=None, prev=None):
        self.data = data
        self._next = nxt
        self._prev = prev


class DoublyLinkedList(object):
    """Class implements a simple doubly linked list."""
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        try:
            if iterable:
                for item in iterable:
                    self.push(item)
        except TypeError:
            raise TypeError("Please enter an object that is iterable.")

    def push(self, data):
        """Insert data at the head of the list."""
        new_node = Node(data)
        new_node._prev = None
        new_node._next = self.head
        if self.head:
            self.head._prev = new_node._next
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def append(self, data):
        """Inserts data at the tail of the list."""
        new_node = Node(data)
        new_node._next = None
        new_node._prev = self.tail
        if self.tail:
            self.tail._next = new_node._prev
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def pop(self):
        """Remove data from the head of the list and return it."""
        pop_node = self.head
        self.head._next._prev = None
        self.head = self.head._next
        return pop_node.data

    def shift(self):
        """Remove data from the tail of the list and return it."""
        shift_node = self.tail
        self.tail._prev._next = None
        self.tail = self.tail._prev
        return shift_node.data

    def remove(self, rem_val):
        """Remove first instance of data from anywhere in the list,
        starting at the head."""
        current = self.head
        try:
            while current.data != rem_val:
                current = current._next
        except AttributeError:
            raise IndexError("That value is not in the list.")
        if current._next is None and current._prev is None:
            self.head = None
            return current.data
        if current._prev is not None:
            current._prev._next = current._next
        if current._next is not None:
            current._next._prev = current._prev
        return current.data
