# -*- coding: utf-8 -*-o
from collections import deque


class Node(object):
    """Building our Node class."""

    def __init__(self, val, left=None, right=None, parent=None):
        """Class implements a node."""
        self.val = val
        self._left = left
        self._right = right
        self._parent = parent

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        try:
            node._parent = self
        except AttributeError:
            pass

    @left.deleter
    def left(self):
        self._left = None

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        try:
            node._parent = self
        except AttributeError:
            pass

    @right.deleter
    def right(self):
        self._right = None


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
        """Insert new node into bst."""
        new_node = Node(val)
        if not self.root:
            self.root = new_node
            self.length = 1
        if node is None:
            node = self.root
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
        """Check if value exists in bst."""
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
        """Determine number of nodes in bst."""
        return self.length

    def _depth_helper(self, start, depth):
        """Helper function to determine depth."""
        if start is None:
            return 0
        pending_list = deque()
        pending_list.append((start, depth))
        while len(pending_list) > 0:
            next_in_line = pending_list.popleft()
            current_node = next_in_line[0]
            depth = next_in_line[1]
            if current_node.left is not None:
                pending_list.append((current_node.left, depth + 1))
            if current_node.right is not None:
                pending_list.append((current_node.right, depth + 1))
        return depth

    def depth(self):
        """Determine max depth of bst."""
        return self._depth_helper(self.root, 1)

    def balance(self):
        """Determine balance of bst."""
        if self.root is None:
            return 0
        left_depth = self._depth_helper(self.root.left, 1)
        right_depth = self._depth_helper(self.root.right, 1)
        return left_depth - right_depth

    def in_order(self, start=None):
        """Returns values in bst using in-order traversal."""
        if self.root is None:
            raise StopIteration("Nothing to traverse.")
        pending_list = []
        cur = start or self.root
        yielded = set()
        while True:
            if cur.left and cur.left.val not in yielded:
                pending_list.append(cur)
                cur = cur.left
            elif cur and cur.val not in yielded:
                yielded.add(cur.val)
                pending_list.append(cur)
                yield cur.val
            elif cur.right and cur.right.val not in yielded:
                pending_list.append(cur)
                cur = cur.right
            else:
                if pending_list:
                    cur = pending_list.pop()
                else:
                    break

    def pre_order(self):
        '''return a generator that will return the values in the tree
        using pre-order traversal, one at a time.'''
        if self.root is None:
            raise StopIteration("Nothing to traverse.")
        pending_list = []
        cur = self.root
        yielded = set()
        while True:
            if cur.val not in yielded:
                yield cur.val
                yielded.add(cur.val)
                pending_list.append(cur)
            if cur.left and cur.left.val not in yielded:
                cur = cur.left
            elif cur.right and cur.right.val not in yielded:
                cur = cur.right
            else:
                if pending_list:
                    cur = pending_list.pop()
                else:
                    break

    def post_order(self):
        '''return a generator that will return the values in the tree
        using pre-order traversal, one at a time.'''
        if self.root is None:
            raise StopIteration("Nothing to traverse.")
        pending_list = []
        cur = self.root
        yielded = set()
        while True:
            if cur.val not in yielded:
                pending_list.append(cur)
            if cur.left and cur.left.val not in yielded:
                cur = cur.left
            elif cur.right and cur.right.val not in yielded:
                cur = cur.right
            elif cur.val not in yielded:
                yield cur.val
                yielded.add(cur.val)
            else:
                if pending_list:
                    cur = pending_list.pop()
                else:
                    break

    def breadth_first(self):
        """Returns values in bst using breadth-first traversal."""
        if self.root is None:
            raise StopIteration("Nothing to traverse.")
        pending_list = deque()
        pending_list.append(self.root)
        while len(pending_list) > 0:
            cur = pending_list.popleft()
            yield cur.val
            if cur.left:
                pending_list.append(cur.left)
            if cur.right:
                pending_list.append(cur.right)

    def _search(self, val):
        cur = self.root
        if not cur:
            raise ValueError("Val not in BST")
        if cur.val == val:
            return cur
        while True:
            if val > cur.val and cur.right is not None:
                cur = cur.right
                if cur.val == val:
                    return cur
            elif val < cur.val and cur.left is not None:
                cur = cur.left
                if cur.val == val:
                    return cur
            else:
                break

    def delete(self, val):
        cur = self._search(val)
        if not cur:
            return
        if self.size() == 1:
            self.root = None
            return
        sub_bst = list(self.in_order(cur))
        index_of_val = sub_bst.index(val)
        if len(sub_bst) == 1:
            if cur.val > cur._parent.val:
                cur._parent.right = None
            else:
                cur._parent.left = None
        else:
            if sub_bst[index_of_val - 1] < cur.val:
                replacement = Node(sub_bst[index_of_val - 1])
                replacement.right = cur.right
            else:
                replacement = Node(sub_bst[index_of_val + 1])
                replacement.left = cur.left
            if cur._parent:
                if cur.val > cur._parent.val:
                    cur._parent.right = replacement
                else:
                    cur._parent.left = replacement
            else:
                self.root = replacement
        self.length -= 1

        def self_balancing(self):
            cur = self.root
            if self.balance(cur) <= 1 or self.balance(cur) >= -1:
                return

        def right_rotation(self, node):
            parent = node.left
            parent.right = node
            return parent

        def left_rotation(self, node):
            parent = node.right
            parent.left = node
            return parent

        def right_left_rotation(self, node):
            node.right = self.right_rotation(node.right)
            node = self.left_rotation(node)
            return node

        def left_right_rotation(self, node):
            node.left = self.left_rotation(node.left)
            node = self.right_rotation(node)
            return node
