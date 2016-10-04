# !/usr/bin/env python
# -*- coding: utf-8 -*-


class HashTable(object):
    """Implement a hash table class in Python."""
    def __init__(self, iterable=None):
        """Set up initialization method on hash table class."""
        self.hash_list = [[] for _ in range(10)]

    def _hash(self, key):
        """Hash the keys in our hash table."""
        if isinstance(key, int):
            return key
        elif isinstance(key, str):
            hashed_value = 0
            for c in key:
                c = ord(c)
                hashed_value += c
            return hashed_value

    def _hash_not_naive(self, key):
        """Hash the keys in our hash table in a better way."""
        pass

    def get(self, key):
        """Returns the value associated with passed key."""
        hashed_key = self._hash(key)
        bucket_idx = hashed_key % len(self.hash_list)
        for k, v in self.hash_list[bucket_idx]:
            if k == key:
                return v

    def set(self, key, val):
        """Adds a new key, value pair to hash table."""
        hashed_key = self._hash(key)
        bucket_idx = hashed_key % len(self.hash_list)
        self.hash_list[bucket_idx].append((key, val))
