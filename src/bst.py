# -*- coding: utf-8 -*-o
from collections import deque

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
        self.root = None
        self.length = 0
        self.depth_left = 0
        self.depth_right = 0
        if iterable is None:
            self.root = None
            return
        for value in iterable:
            self.insert(value)

    def insert(self, val, node=None):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
            self.length = 1
        if node is None:
            node = self.root
        if not node:
            self.root = new_node
            self.length += 1
            return
        if val > node.val:
            if not node.right:
                node.right = new_node
                self.length += 1
            else:
                self.insert(val, node.right)
        elif val < node.val:
            if not node.left:
                node.left = new_node
                self.length += 1
            else:
                self.insert(val, node.left)

    def contains(self, val):
        current_node = self.root
        if current_node is None:
            return False
        if val == current_node.val:
            return True
        while True:
            if val > current_node.val and current_node.right is not None:
                current_node = current_node.right
                if current_node.val == val:
                    return True
            elif val < current_node.val and current_node.left is not None:
                current_node = current_node.left
                if current_node.val == val:
                    return True
            else:
                return False

    def size(self):
        return self.length

    # def depth(self, root):
        # if self.root is None:
            # return 0
        # if self.root.right is None and self.root.left is None:
            # return 1
        # self.depth = max(self.depth(self.root.right), self.depth(self.root.left)
        # return self.depth

    def depth(self):
        if self.root is None:
            return 0
        pending_list = deque()
        pending_list.append((self.root, 1))
        while len(pending_list) > 0:
            next_in_line = pending_list.popleft()
            current_node = next_in_line[0]
            depth = next_in_line[1]
            if current_node.left is not None:
                pending_list.append((current_node.left, depth + 1))
            if current_node.right is not None:
                pending_list.append((current_node.right, depth + 1))
        return depth

    def balance(self):
        pass
