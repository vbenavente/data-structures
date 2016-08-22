# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dll import DoublyLinkedList


class Deque(object):
    """Deque implements a simple Python deque data structure."""

    def __init__(self, iterable=None):
        self.dll = DoublyLinkedList(iterable)

    def append(self, data):
        """Append a node containing data to the head(end) of the deque."""
        pass

    def appendleft(self, data):
        """Append a node containing data to the tail(front) of the deque."""
        pass

    def pop(self):
        """Remove a value from the head(end) of the deque and return it.

        Will raise an exception if the deque is empty."""
        pass

    def popleft(self):
        """Remove a value from the tail(front) of the deque and return it.

        Will raise an exception if the deque is empty."""
        pass

    def peek(self):
        """Returns the value of the head(end) of the deque.

        Returns None if the deque is empty."""
        pass

    def peekleft(self):
        """Returns a value from the tail(front) of the deque.

        Returns None if the deque is empty."""
        pass

    def size(self):
        """Returns the count of nodes in the queue, 0 if empty."""
        count = 0
        current = self.dll.head
        while current is not None:
            count += 1
            current = current._next
        return count
