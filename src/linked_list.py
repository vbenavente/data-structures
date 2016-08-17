# -*- coding: utf-8 -*-
"""This file implements a basic linked list data structure."""
import sys


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
        try:
            if data:
                for item in data:
                    self.push(item)
        except TypeError:
            raise TypeError('Please enter an object that is iterable.')

    def push(self, data):
        """Function builds push method of LinkedList class."""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        return self.head

    def pop(self):
        """Function builds pop method of LinkedList class."""
        pop_node = self.head
        self.head = self.head.next_node
        return pop_node

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
        while current is not None and data != current.data:
            current = current.next_node
        return current.data

    def remove(self, node):
        """Function build remove method of LinkedList class."""
        node.data = node.next_node
        next_node = node.next_node.next_node
        return next_node.data

    # def display():

if __name__ == '__main__':
    LinkedList(sys.argv[1])
