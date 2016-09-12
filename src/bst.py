# -*- coding: utf-8 -*-
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

    def insert(self, val, node=None):
        new_node = Node(val)
        if node is None:
            node = self.root
        if not node:
            self.root = new_node
            return
        if val > node.val:
            if not node.right:
                node.right = new_node
            else:
                self.insert(val, node.right)
        elif val < node.val:
            if not node.left:
                node.left = new_node
            else:
                self.insert(val, node.left)

    def contains(self, val):
        pass

    def size(self):
        pass

    def depth(self):
        pass

    def balance(self):
        pass
