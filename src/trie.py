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

    def conatins(self, token):
        pass
