# -*- coding: utf-8 -*-
"""The following code tests our trie tree implementation."""
from __future__ import unicode_literals


def test_trie_node_init_no_values_one():
    """Test the trie node init method, lookup value with no input values."""
    from trie import Node
    test_case = Node()
    assert test_case.lookup == {}


def test_trie_node_init_no_values_two():
    """Test the trie node init method, end value with no input values."""
    from trie import Node
    test_case = Node()
    assert test_case.end is False


def test_trie_node_init_inputs_one():
    """Test the trie node init method, lookup value with appropriate input."""
    from trie import Node
    test_case = Node("a", True)
    assert test_case.lookup["a"] == []


def test_trie_node_init_inputs_two():
    """Test the trie node init method, end value with appropriate input."""
    from trie import Node
    test_case = Node("a", True)
    assert test_case.end is True


def test_trie_class_init():
    """Test that the Trie class inits correctly."""
    from trie import Trie
    test_case = Trie()
    assert test_case.root.lookup == {}
