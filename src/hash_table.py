# !/usr/bin/env python
# -*- coding: utf-8 -*-


class HashTable(object):
    """Implement a hash table class in Python."""
    def __init__(self, iterable=None, size=10, hashing_algorithm='default'):
        """Set up initialization method on hash table class."""
        algorithms = {
            'default': '_hash',
            'strong': '_hash_not_naive'
        }
        try:
            self.hashing_algorithm = algorithms[hashing_algorithm]
        except KeyError as e:
            e.args = ('Hashing algorithm not found', )
            raise
        self.hash_list = [[] for _ in range(size)]

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
        """Hash the keys in our hash table in a different way."""
        if isinstance(key, int):
            return key
        elif isinstance(key, str):
            hashed_value = ''
            for c in key:
                hashed_value += str(ord(c))
            return int(hashed_value)

    def get(self, key):
        """Returns the value associated with passed key."""
        hashed_key = getattr(self, self.hashing_algorithm)(key)
        bucket_idx = hashed_key % len(self.hash_list)
        for k, v in self.hash_list[bucket_idx]:
            if k == key:
                return v

    def set(self, key, val):
        """Adds a new key, value pair to hash table."""
        hashed_key = getattr(self, self.hashing_algorithm)(key)
        bucket_idx = hashed_key % len(self.hash_list)
        self.hash_list[bucket_idx].append((key, val))
