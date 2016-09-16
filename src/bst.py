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
        """Returns true if there is a left child."""
        return self.left

    def has_right_child(self):
        """Returns true if there is a right child."""
        return self.right

    def _insert(self, val, data=None):
        """Helper method to BST.insert method."""
        if val < self.val:
            if self.has_left_child():
                self.left._insert(val)
            else:
                self.left = Node(val, data)
        else:
            if self.has_right_child():
                self.right._insert(val, data)
            else:
                self.right = Node(val)
        ld = self.left.depth if self.left else 0
        rd = self.right.depth if self.right else 0
        self.depth = 1 + max(ld, rd)

    def _in_order(self):
        """
        This internal method is a generator that will output in order traversal
        of a binary tree(left child, parent, right child), one value at a time.
        """
        try:
            for node in self.left._in_order():
                if node is None:
                    pass
                else:
                    yield node
        except AttributeError:
            pass
        yield self.val
        try:
            for node in self.right._in_order():
                if node is None:
                    pass
                else:
                    yield node
        except AttributeError:
            pass

    def _pre_order(self):
        """
        This internal method is a generator that will output preorder traversal
        of a binary tree(parent, left child, right child), one value at a time.
        """
        yield self.val
        try:
            for node in self.left._pre_order():
                if node is None:
                    pass
                else:
                    yield node
        except AttributeError:
            pass
        try:
            for node in self.right._pre_order():
                if node is None:
                    pass
                else:
                    yield node
        except AttributeError:
            pass

    def _post_order(self):
        """
        This internal method is a generator that will output postorder traversal
        of a binary tree(left child, right child, parent), one value at a time.
        """
        try:
            for node in self.left._post_order():
                if node is None:
                    pass
                else:
                    yield node
        except AttributeError:
            pass
        try:
            for node in self.right._post_order():
                if node is None:
                    pass
                else:
                    yield node
        except AttributeError:
            pass
        yield self.val


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

    def insert(self, val, data=None):
        """Inserts a value  into the BST.  If the value is already in
        the BST it will be ingored."""
        if not self.contains(val):
            if self.root:
                self.root._insert(val, data)
            else:
                self.root = Node(val, data)
            self.length += 1

    def contains(self, val):
        """Will return True if val is in the BST, or False if it's not."""
        try:
            return self._contains(val, self.root)
        except AttributeError:
            pass

    def _contains(self, val, current_node):
        """Helper method to contains, recursively called and returns True
        if we find the node we're looking for, False if not."""
        if val == current_node.val:
            return True
        elif current_node.right and val > current_node.val:
            return self._contains(val, current_node.right)
        elif current_node.left and val < current_node.val:
            return self._contains(val, current_node.left)
        else:
            return False

    def size(self):
        """Will return the integer size of the BST, zero if BST is empty."""
        return self.length

    def __len__(self):
        """Returns size of tree using builtin length method."""
        return self.length

    def depth(self, starting_point=None):
        """Will return the depth of the tree by counting "levels".  An empty
        BST will return 0, a BST with 1 value will return 1, a BST with 2
        values will return 2, and the value will fluctuate from then on
        depending on the branch layout."""
        if starting_point is None:
            starting_point = self.root
        # import pdb; pdb.set_trace();
        try:
            ld = starting_point.left.depth
        except AttributeError:
            ld = 0
        try:
            rd = starting_point.right.depth
        except AttributeError:
            rd = 0
        try:
            md = starting_point.depth
        except AttributeError:
            md = 0
        return max(ld, rd, md)

    def balance(self, starting_point=None):
        """Will return an integer that's positive or negative that represents
        the difference between depth on both sides from the root."""
        if starting_point is None:
            starting_point = self.root
        return starting_point.left - starting_point.right

    def in_order(self, starting_point=None):
        """
        This function will return a generator that will return the values
        of the tree using in-order traversal, one value at a time.
        """
        if starting_point is None:
            starting_point = self.root
        return starting_point._in_order()

    def pre_order(self, starting_point=None):
        """
        This function will return a generator that will return the values
        of the tree using pre_order traversal, one value at a time.
        """
        if starting_point is None:
            starting_point = self.root
        return starting_point._pre_order()

    def post_order(self, starting_point=None):
        """
        This function will return a generator that will return the values
        of the tree using post_order traversal, one value at a time.
        """
        if starting_point is None:
            starting_point = self.root
        return starting_point._post_order()

    def breadth_first(self, starting_point=None):
        """
        This internal method is a generator that will output breadth first
        traversal of a binary tree(left child, right child, parent),
        one value at a time.
        """
        from dll import DoublyLinkedList
        unvisited = DoublyLinkedList()
        if starting_point is None:
            starting_point = self.root
        elif self.contains(starting_point) is False:
            raise IndexError('Starting point is not in the tree')
        unvisited.push(starting_point)
        visited = []
        while unvisited.size() > 0:
            current = unvisited.shift()
            if current not in visited:
                visited.append(current)
                if current.left:
                    unvisited.push(current.left)
                if current.right:
                    unvisited.push(current.right)
                yield current.val
