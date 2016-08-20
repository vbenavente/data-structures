# -*- coding: utf-8 -*-
"""File implements a basic linked list data structure."""
from __future__ import unicode_literals


class Node(object):
    """Building our Node class."""

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):
    """Building our LinkedList class."""

    def __init__(self, data=None):
        self.head = None
        if data is not None:
            try:
                for item in data:
                    self.push(item)
            except TypeError:
                raise TypeError('Please enter an object that is iterable.')

    def push(self, data):
        """Insert data at the head of the list."""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def pop(self):
        """Remove data from the head of the list."""
        pop_node = self.head
        try:
            self.head = self.head.next_node
        except AttributeError:
            raise IndexError("You cannot pop from an empty list.")
        return pop_node.data

    def size(self):
        """Finds the size of our list."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next_node
        return count

    def __len__(self):
        """Binds .size to __len__ builtin so len() works."""
        return self.size()

    def search(self, data):
        """Feturns the node that a specific value is in."""
        current = self.head
        try:
            while data != current.data:
                current = current.next_node
            return current
        except AttributeError:
            raise IndexError("That value is not in the list.")

    def remove(self, node):
        """Removes a specific node from the list."""
        current = self.head
        try:
            while node.data != current.data:
                previous = current
                current = current.next_node
            previous.next_node = current.next_node.next_node
            return current
        except AttributeError:
            raise IndexError("That value is not in the list.")

    def display(self):
        """Display the list to the command line like a tuple literal."""
        current = self.head
        accumulator = "("
        while current is not None:
            accumulator = "".join(accumulator + str(current.data) + ", ")
            current = current.next_node
        accumulator = accumulator[:-2]
        accumulator += ")"
        return accumulator
