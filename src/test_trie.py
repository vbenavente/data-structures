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


def test_insert_one():
    """Test new token inserted in trie."""
    trie = Trie()
    trie.insert('cow')
    assert trie.root['c'] == {'o': {'w': {'#': '#'}}}


def test_insert_multiple():
    """Test multiple tokens inserted in trie."""
    trie = Trie()
    trie.insert('cow')
    trie.insert('coward')
    trie.insert('template')
    assert trie.root['c'] == {
        'o': {
            'w': {
                '#': '#',
                'a': {'r': {'d': {'#': '#'}}},
            }
        }
    }


def test_contain_true():
    """Test if a trie contains a word."""
    trie = Trie(['cow', 'coward', 'company'])
    assert trie.contains('cow')


def test_contain_false_1():
    """Test if a trie contains a word."""
    trie = Trie(['cow', 'coward', 'company'])
    assert not trie.contains('co')


def test_contain_false_2():
    """Test if a trie contains a word."""
    trie = Trie(['cow', 'coward', 'company'])
    assert not trie.contains('something')
