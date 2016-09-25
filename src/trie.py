# -*- coding: utf-8 -*-
"""The following code implements a trie tree in python."""
from __future__ import unicode_literals


class Node(object):
    """Implements nodes for our Trie tree."""

    def __init__(self, value=None, end=False):
        """Creates an instance of our trie node class."""
        self.lookup = {}
        if value is not None:
            self.lookup[value] = []
        self.end = end


class Trie(object):
    """Trie tree class with supporting methods."""

    def __init__(self):
        """Initializes an empty Trie tree."""
        self.root = Node()

    def insert(self, value):
        """Inserts a new value into our trie tree."""
        if not isinstance(value, str):
            raise TypeError("Input must be a string")
        value.reserse()
        first = value.pop()
        if first in self.root.####
        for character in value:
            # check for membership of char in root node.  If found, follow
            # that relationship
            # if not found, add the key w/ new node as
            pass

    def contains(self, value):
        """Returns true if value is in trie, false if not."""

    def depth_first_traversal(self, start=None):
        """Performs a depth-first traversal of our trie beginning at the
        node we specify as start, otherwise we begin at the root."""
        if start is None:
            start = self.root
        traverse = []

        return traverse
