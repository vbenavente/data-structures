# -*- coding: utf-8 -*-


class Trie(object):
    def __init__(self, iterable=None):
        self.root = {}
        if iterable:
            for i in iterable:
                self.insert(i)

    def insert(self, token):
        start = self.root
        for letter in token:
            start = start.setdefault(letter, {})
        start['#'] = '#'

    def contains(self, token):
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
