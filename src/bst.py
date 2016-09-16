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
        return self.left

    def has_right_child(self):
        return self.right

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
        if self.root:
            self._insert(val, self.root, data)
        else:
            self.root = Node(val, data)
        self.length += 1

    def _insert(self, val, current_node, data=None):
        current_node = current_node
        if val < current_node.val:
            if current_node.has_left_child():
                return self._insert(val, current_node.left)
            else:
                current_node.left = Node(val)
        else:
            if current_node.has_right_child():
                return self._insert(val, current_node.right)
            else:
                current_node.right = Node(val)

    def contains(self, val):
        """Will return True if val is in the BST, or False if it's not."""
        return self._contains(val, self.root)

    def _contains(self, val, current_node):
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
        return max(starting_point.left, starting_point.right)

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
            if current not in vistied:
                visited.append(current)
                if current.left:
                    unvisited.push(current.left)
                if current.right:
                    unvisited.push(current.right)
                yield current
