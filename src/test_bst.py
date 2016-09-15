# -*- coding: utf-8 -*-
"""File tests a binary search tree data structure."""
from __future__ import unicode_literals

from collections import namedtuple
import pytest
import random
import string


EDGE_CASES = [
    {},
    [],
    {'a': 0},
    [1, 2, 3],
    ''
]

INT_CASES = [random.sample(range(1000),
             random.randrange(2, 100)) for n in range(10)
             ]


STR_CASES = [random.sample(string.printable,
             random.randrange(2, 100)) for n in range(10)
             ]

TEST_CASES = INT_CASES + STR_CASES

MyBSTFix = namedtuple(
    'BSTFixture',
    ('bin_tree', 'input_val', 'length')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def bst(request):
    '''return an empty Simple Graph'''
    from bst import BinarySearchTree
    bin_tree = BinarySearchTree()
    if type(request.param) is not int():
        length = len(request.param)
    for val in request.param:
        input_val = val
    return MyBSTFix(bin_tree, input_val, length)


def test_bst_init_node(bst):
    from bst import Node
    a = Node(bst.input_val)
    assert bst.input_val == a.val


def test_bst_init_node_has_left(bst):
    from bst import Node
    a = Node(bst.input_val, bst.input_val, bst.input_val, bst.input_val)
    assert a.has_left_child() == bst.input_val


def test_bst_init_node_has_right(bst):
    from bst import Node
    a = Node(bst.input_val, bst.input_val, bst.input_val, bst.input_val)
    assert a.has_right_child() == bst.input_val


def _test_bst_init_empty_tree(bst):
    assert bst.bin_tree.root is None


def test_bst_init_bin_tree():
    from bst import BinarySearchTree
    a = BinarySearchTree(1)
    assert a.root.val == 1


def test_bst_insert(bst):
    bst.bin_tree.insert(bst.input_val)
    assert bst.bin_tree.root.val == bst.input_val


def test_bst_insert_with_existing_node_right(bst):
    bst.bin_tree.insert(bst.input_val)
    bst.bin_tree.insert(bst.input_val * 2)
    assert bst.bin_tree.root.right


def test_bst_insert_with_existing_node(bst):
    bst.bin_tree.insert(bst.input_val * 2)
    bst.bin_tree.insert(bst.input_val)
    assert bst.bin_tree.root.left
