# -*- coding: utf-8 -*-
from collections import OrderedDict


class Node(object):
    """Building our Node class."""

    def __init__(self, val, left=None, right=None):
        """Class implements a node."""
        self.val = val
        self.left = left
        self.right = right


class BST(object):
    """Class implements a binary search tree data structure in Python."""

    def __init__(self, iterable=None):
        """Init method of bst class."""
        if iterable is None:
            self.root = None
            return

    def insert(self, val):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
        else:
            if val > self.root.val:
                if not self.root.right:
                    self.root.right = new_node

        # for key, val in self.bst:
        #     if val > self.bst[key] and
        #     current = self.bst.val
        #     if val > current

    def contains(self, val):
        pass

    def size(self):
        pass

    def depth(self):
        pass

    def balance(self):
        pass
