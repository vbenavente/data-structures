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
            self.length += 1
        else:
            self.root = root

    def __iter__(self):
        """Allows this data structures to be iterated on."""
        return self.root.__iter__()

    def node_list(self, starting_point=None):
        """Steps through the BST depth-first and returns a list of nodes
        in the BST.

        Expects a starting point == value of a node in the graph."""
        from dll import DoublyLinkedList
        dll = DoublyLinkedList()
        if starting_point is None:
            starting_point = self.root
        # if self.has_node(starting_point) is False:
        #     raise IndexError("That starting point is not in the graph.")
        dll.push(starting_point)
        result = []
        while dll.size() > 0:
            working_node = dll.pop()
            if working_node not in result:
                result.append(working_node)
                for node in self.neighbors(working_node):
                    dll.push(node)
        return result

    def insert(self, val, data=None):
        """Inserts a value  into the BST.  If the value is already in
        the BST it will be ingored."""
        if self.root:
            self._insert(val, data, self.root)
        else:
            self.root = Node(val, data)
        self.length += 1

    def _insert(self, val, current_node, data=None):
        if val < current_node.val:
            if current_node.has_left_child():
                self._insert(val, data, current_node.left)
            else:
                current_node.left = Node(val, data, parent=current_node)
        else:
            if current_node.has_right_child():
                self._insert(val, data, current_node)
            else:
                current_node.right = Node(val, data, parent=current_node)

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

    def depth(self):
        """Will return the depth of the tree by counting "levels".  An empty
        BST will return 0, a BST with 1 value will return 1, a BST with 2
        values will return 2, and the value will fluctuate from then on
        depending on the branch layout."""

    def balance(self, starting_point=None):
        """Will return an integer that's positive or negative that represents
        the difference between depth on both sides from the root."""
        if starting_point is None:
            starting_point = self.root
        left_total = self._balance(starting_point.left)
        right_total = self._balance(starting_point.right)
        return left_total - right_total

    def _balance(self, starting_point):
        """Steps through the BST breadth-first and returns the len of the
        resulting list.

        Expects a starting point == value of a node in the BST.  This mehod
        adapted from Derek's previous simple_graph."""
        from dll import DoublyLinkedList
        dll = DoublyLinkedList()
        if self.contains(starting_point) is False:
            raise IndexError("That starting point is not in the graph.")
        dll.push(starting_point)
        result = []
        while dll.size() > 0:
            working_node = dll.shift()
            if working_node not in result:
                result.append(working_node)
                for node in self._neighbors(working_node):
                    dll.push(node)
        return len(result)

    def _neighbors(self, node):
        """Finds and returns the children of a given node."""
        neighbors = []
        if node.left:
            neighbors.append(node.left)
        if node.right:
            neighbors.append(node.right)
        return neighbors

    def count(self, starting_point=None):
        """Recursively explores the BST and returns a count of the nodes
        'below' the starting point in the BST."""
        if starting_point is None:
            starting_point = self.root
