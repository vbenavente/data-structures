# -*- coding: utf-8 -*-
"""File implements a binary search tree data structure."""
from __future__ import unicode_literals


class Node(object):
    """Example node class with example @property decorators

    pieces of this code are significantly wrong (parent deletion for
    instance) and you should test your implementation throughly"""

    def __init__(self, val, data=None, left=None, right=None,
                 parent=None):
        """sets self.whatever values for instantiating instances of
        the class"""
        self.val = val
        self._left = left
        self._right = right
        self._parent = parent
        self.data = data
        self.depth = 1

    @property
    def left(self):
        """value getter for _left
        syntax: node.left returns _left's value"""
        return self._left

    @left.setter
    def left(self, other):
        """value setter for _left, allows us to say 'set node.left = X'
        elsewhere in our code and not have it throw wrenches at us"""
        self._left = other
        other._parent = self

    @left.deleter
    def left(self):
        """allows us to say 'del node.left' else where in our code and get this
        outcome"""
        try:
            self._left._parent = None
        except AttributeError:
            pass
        self._left = None

    @property
    def right(self):
        """returns value of _right"""
        return self._right

    @right.setter
    def right(self, other):
        """sets value of _right and right's parent"""
        self._right = other
        other._parent = self

    @right.deleter
    def right(self):
        try:
            self._right._parent = None
        except AttributeError:
            pass
        self._right = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, other):
        self._parent = other
        if other.val < self.val:
            other._left = self
        else:
            other._right = self

    def has_left_child(self):
        """Returns true if there is a left child."""
        return self.left

    def has_right_child(self):
        """Returns true if there is a right child."""
        return self.right

    def _insert(self, val, data=None):
        """Helper method to BST.insert method."""
        try:
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
        except TypeError:
            raise(TypeError('Insert values must be the same type'))

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
        Returns a generator that will output preorder traversalof a binary
        tree(parent, left child, right child), one value at a time.
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
        Returns a generator that will output postorder traversalof a binary
        tree(left child, right child, parent), one value at a time.
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
        """Inserts a value into the BST.  If the value is already in
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
        try:
            if val == current_node.val:
                return True
            elif current_node.right and val > current_node.val:
                return self._contains(val, current_node.right)
            elif current_node.left and val < current_node.val:
                return self._contains(val, current_node.left)
            else:
                return False
        except TypeError:
            raise(TypeError('Node values must be the same type'))

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
        return starting_point.left.depth - starting_point.right.depth

    def in_order(self, starting_point=None):
        """
        This function will return a generator that will return the values
        of the tree using in-order traversal, one value at a time.
        """
        if self.length is None:
            raise IndexError("You can't in-order traverse an empty Tree.")
        if starting_point is None:
            starting_point = self.root
        return starting_point._in_order()

    def pre_order(self, starting_point=None):
        """
        This function will return a generator that will return the values
        of the tree using pre_order traversal, one value at a time.
        """
        if self.length is None:
            raise IndexError("You can't pre-order traverse an empty Tree.")
        if starting_point is None:
            starting_point = self.root
        return starting_point._pre_order()

    def post_order(self, starting_point=None):
        """
        This function will return a generator that will return the values
        of the tree using post_order traversal, one value at a time.
        """
        if self.length is None:
            raise IndexError("You can't post-order traverse an empty Tree.")
        if starting_point is None:
            starting_point = self.root
        return starting_point._post_order()

    def breadth_first(self, starting_point=None):
        """
        This internal method is a generator that will output breadth first
        traversal of a binary tree(left child, right child, parent),
        one value at a time.
        """
        if self.length is None:
            raise IndexError("You can't breadth-first traverse an empty Tree.")
        from dll import DoublyLinkedList
        unvisited = DoublyLinkedList()
        if starting_point is None:
            starting_point = self.root
        elif self.contains(starting_point) is False:
            raise IndexError('Starting point is not in the Tree.')
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

    def delete(self, val):
        """Removes a node from the Tree, returns None."""
        delete_me = self.find_node(val)
        if delete_me is False:
            return "That node is not in the BST."
        left_childs = self.in_order(delete_me.left)
        right_childs = self.in_order(delete_me.right)
        left_list = []
        for child in left_childs:
            left_list.append(child)
        left_choice = left_list[-1]
        right_choice = right_childs.__next__()
        a = right_choice - val
        b = val - left_choice
        if a > b:
            left_choice = self.find_node(left_choice)
            if self.root == delete_me:
                self.root = left_choice
            if left_choice.left is not None:
                left_choice.left.parent = left_choice.parent
            delete_me.val = left_choice.val
        else:
            right_choice = self.find_node(right_choice)
            # import pdb; pdb.set_trace()
            if self.root == delete_me:
                self.root = right_choice
            if right_choice.right is not None:
                right_choice.right.parent = right_choice.parent
            delete_me.val = right_choice.val
        self._check_balance(delete_me)
        self._update_children(delete_me)
        self.length -= 1

    def find_node(self, val):
        """Will return the node with the val we asked for or False if it
        isn't in the BST."""
        return self._find_node(val, self.root)

    def _find_node(self, val, current_node):
        """Helper method to find_node, recursively called and returns the node
        or False if it isn't in the BST."""
        try:
            if val == current_node.val:
                return current_node
            elif current_node.right and val > current_node.val:
                return self._find_node(val, current_node.right)
            elif current_node.left and val < current_node.val:
                return self._find_node(val, current_node.left)
            else:
                return False
        except TypeError:
            raise(TypeError('Node values must be the same type'))

    def _left_rotation(self, pivot_parent):
        """Performs a left rotation on a given section of our BST."""
        a = pivot_parent
        b = pivot_parent.right_child
        try:
            z = pivot_parent.parent
        except AttributeError:
            z = None
            self.root = b
        try:
            w = pivot_parent.right_child.left_child
        except AttributeError:
            w = None
        b.left = a
        a.right = w
        b.parent = z

    def _right_rotation(self, pivot_parent):
        """Performs a right rotation on a given section of our BST."""
        a = pivot_parent
        b = pivot_parent.left_child
        try:
            z = pivot_parent.parent
        except AttributeError:
            z = None
            self.root = b
        try:
            w = pivot_parent.left_child.right_child
        except AttributeError:
            w = None
        a.left = w
        b.right = a
        b.parent = z

    def _check_balance_and_call(self, starting_point, previous=None):
        """Checks the balance of parents of a given node up to the root, calls
        _determine_rotations_and_call if rotations needed."""
        bal = self.balance(starting_point)
        if bal > 1:
            self._determine_rotations_and_call(starting_point, previous)
            break
        if bal < -1:
            self._determine_rotations_and_call(starting_point, previous)
            break
        if starting_point.parent is None:
            break
        self._check_balance_and_call(starting_point.parent, starting_point)
        break
        # TODO - determine which child should be previous if deletion

    def _determine_rotations_and_call(self, starting_point, previous):
        """Determine which rotations are needed and call them, then call
        _update_balance."""
        start_bal = self.balance(starting_point)
        if previous is not None:
            prev_bal = self.balance(previous)
        else:
            prev_bal = 0
        if start_bal < -1:
            if prev_bal > 0:
                self._right_rotation(starting_point)
            self._left_rotation(starting_point)
        else:
            if prev_bal < 0:
                self._left_rotation(starting_point)
            self._right_rotation(starting_point)

    def _update_balance(self, starting_point):
        """Updates the balance of the BST, it's intended this will be called
        on self.root. Recursively calls itself until there are no more
        children to update, then resets the depth value of all nodes."""
        if starting_point.left:
            left_depth = self._update_balance(starting_point.left)
        else:
            left_depth = 0
        if starting_point.right:
            right_depth = self._update_balance(starting_point.right)
        else:
            right_depth = 0
        starting_point.depth = max(left_depth, right_depth) + 1
        return starting_point.depth
