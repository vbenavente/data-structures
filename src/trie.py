# -*- coding: utf-8 -*-
from collections import deque, OrderedDict


class Trie(object):
    def __init__(self, iterable=None):
        self.root = OrderedDict()
        if iterable:
            for i in iterable:
                self.insert(i)

    def insert(self, token):
        start = self.root
        for letter in token:
            start = start.setdefault(letter, OrderedDict())
        start['#'] = '#'

    def contains(self, token):
        """Verify if a token is in the trie."""
        start = self.root
        counter = 0
        while counter < len(token):
            try:
                start = start[token[counter]]
            except KeyError:
                return False
            counter += 1
            try:
                return start['#'] == '#'
            except KeyError:
                pass
        return False

    def search(self, char):
        """Returns the dict that start by the passed in char."""
        pending_list = deque()
        for k, v in self.root.items():
            pending_list.append((k, v))
        while len(pending_list) > 0:
            cur = pending_list.popleft()
            if char == cur[0]:
                return cur[1]
            if type(cur[1]) is dict:
                for k, v in cur[1].items():
                    pending_list.append((k, v))

    def traversal(self, start=None):
        import pdb; pdb.set_trace()
        start = self.search(start) if start else self.root
        if not start:
            raise KeyError('Start point not found')
        pending_list = []
        for k, v in reversed(start.items()):
            pending_list.append((k, v))
        while len(pending_list) > 0:
            start = pending_list.pop()
            if len(start[1]) == 1 and start[1].get('#') == '#':
                yield start[0]
            else:
                for k, v in reversed(start[1].items()):
                    pending_list.append((k, v))
