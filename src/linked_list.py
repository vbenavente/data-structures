# -*- coding: utf-8 -*-
"""This file implements a basic linked list data structure."""
from __future__ import unicode_literals


class Node(object):
    """This builds our Node class."""

    def __init__(self, data):
        """Initial setup of Node objects."""
        self.data = data
        self.next_node = None


class LinkedList(object):
    """This builds LinkedList class."""

    def __init__(self, data=None):
        """Initial setup of LinkedList class."""
        self.head = None
        if data is not None:
            try:
                for item in data:
                    self.push(item)
            except TypeError:
                raise TypeError('Please enter an object that is iterable.')

    def push(self, data):
        """Function builds push method of LinkedList class."""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def pop(self):
        """Function builds pop method of LinkedList class."""
        pop_node = self.head
        self.head = self.head.next_node
        return pop_node.data

    def size(self):
        """Function builds size method of LinkedList class."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next_node
        return count

    def __len__(self):
        """Function binds LinkedList to __len__ builtin so len() works."""
        return self.size()

    def search(self, data):
        """Function builds search method of LinkedList class."""
        current = self.head
        try:
            while current is not None and data != current.data:
                current = current.next_node
            return current
        except:
            return None

    def remove(self, node):
        """Function build remove method of LinkedList class."""
        current = self.head
        while current is not None and node.data != current.data:
            previous = current
            current = current.next_node
        previous.next_node = current.next_node.next_node
        return current

    def display(self):
        """Function builds display method of LinkedList class."""
        current = self.head
        accumulator = []
        while current is not None:
            accumulator.append(str(current.data))
            current = current.next_node
        accum_string = ", ".join(accumulator)
        display_string = "({})".format(accum_string)
        return display_string
