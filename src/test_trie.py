# -*- coding: utf-8 -*-
from trie import Trie


def test_trie_init_empty():
    """Test an empty trie is created."""
    trie = Trie()
    assert len(trie.root) == 0


def test_trie_with_iterable():
    """Test trie instance created with iterable."""
    trie = Trie(['cow', 'tub', 'hot'])
    assert len(trie.root) == 3


def test_insert():
    """Test new token inserted in trie."""
    trie = Trie()
    trie.insert('cow')
    assert trie.root['c'] == {'o': {'w': {'#': '#'}}}
