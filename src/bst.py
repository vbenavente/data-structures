# -*- coding: utf-8 -*-
"""File implements a binary search tree data structure."""
from __future__ import unicode_literals


class Node(object):

    def __init__(self, val, data=None, left=None, right=None,
                 parent=None):
        """Instantiates a Node class object for use in our BST.

        Data is a ride-along additional value holder that may be used
        later."""

        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.data = data
        self.depth = 1

        def has_left_child(self):
            return self.left.val

        def has_right_child(self):
            return self.right.val


class BinarySearchTree(object):
    """BinarySearchTree implements a Binary Search Tree data structure
    and associated methods."""

    def __init__(self, root=None):
        """Create an instance of our Binary Search Tree w/ supplied
        input, or an emptry tree."""
        self.length = 0
        if root:
            self.root = Node(root)
            self.length = 1
        else:
            self.root = root
            self.length = 0

    def insert(self, val, data=None):
        """Inserts a value  into the BST.  If the value is already in
        the BST it will be ingored."""
        if self.root:
            self._insert(val, data, self.root)
        else:
            self.root = Node(val, data)
        self.length += 1

    def _insert(self, val, current_node, data=None):
        keep_going = True
        while keep_going:
            if val < current_node.val:
                if current_node.has_left_child():
                    new_depth = self._insert(val, data, current_node.left)
                else:
                    current_node.left = Node(val, data, parent=current_node)
                    keep_going = False
            elif val > current_node.val:
                if current_node.has_right_child():
                    new_depth = self._insert(val, data, current_node)
                else:
                    current_node.right = Node(val, data, parent=current_node)
                    keep_going = False
            else:
                keep_going = False
        self.length += 1
        self.depth = new_depth + 1
        return self.depth

    def contains(self, val):
        """Will return True if val is in the BST, or False if it's not."""
        for node in self.__iter__():
            if node.val == val:
                return True
        return False

    def size(self):
        """Will return the integer size of the BST, zero if BST is empty."""
        return self.length

    def __len__(self):
        """Calls self.size and returns value from there."""
        return self.size()

    def depth(self, starting_point=None):
        """Will return the depth of the tree by counting "levels".  An empty
        BST will return 0, a BST with 1 value will return 1, a BST with 2
        values will return 2, and the value will fluctuate from then on
        depending on the branch layout."""
        if starting_point is None:
            starting_point = self.root
        return max(starting_point.left, starting_point.right)

    def balance(self, starting_point=None):
        """Will return an integer that's positive or negative that represents
        the difference between depth on both sides from the root."""
        if starting_point is None:
            starting_point = self.root
        return starting_point.left - starting_point.right
