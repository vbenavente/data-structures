# -*- coding: utf-8 -*-
"""File implements a binary search tree data structure."""
from __future__ import unicode_literals


class Node(object):

    def __init__(self, val, left=None, right=None,
                 parent=None, data=None):
        """Instantiates a Node class object for use in our BST.

        Data is a ride-along additional value holder that may be used
        later."""

        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.data = data


class BinarySearchTree(object):
    """BinarySearchTree implements a Binary Search Tree data structure
    and associated methods."""

    def __init__(self, root=None):
        """Create an instance of our Binary Search Tree w/ supplied
        input, or an emptry tree."""
        self.root = root

    def __iter__(self):
        """Allows this data structures to be iterated on."""
        return self.root.__iter__()

    def insert(self, val):
        """Inserts a value  into the BST.  If the value is already in
        the BST it will be ingored."""

    def contains(self, val):
        """Will return True if val is in the BST, or False if it's not."""

    def size(self):
        """Will return the integer size of the BST, zero if BST is empty."""

    def __len__(self):
        """Calls self.size and returns value from there."""
        return self.size

    def depth(self):
        """Will return the depth of the tree by counting "levels".  An empty
        BST will return 0, a BST will 1 value will return 1, a BST with 2
        values will return 2, and the value will fluctuate from then on
        depending on the branch layout."""

    def balance(self):
        """Will return an integer that's positive or negative that represents
        the difference between depth on both sides from the root."""
