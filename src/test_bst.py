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
    ('bin_tree', 'input_val', 'error_gen', 'length')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def full_bst(request):
    '''return an empty Simple Graph'''
    from bst import BinarySearchTree
    bin_tree = BinarySearchTree()
    length = len(request.param)
    for val in request.param:
        bin_tree.insert(val)
    if request.param or isinstance(request.param[0], int):
        input_val = 999
        error_gen = 'STRING!'
    else:
        input_val = 'STRING!!'
        error_gen - 999
    return MyBSTFix(bin_tree, input_val, error_gen, length)


@pytest.fixture(scope='function', params=[1, 5, 9, 15, 25, 'a', 'd', 'q'])
def empty_bst(request):
    '''return an empty Simple Graph'''
    from bst import BinarySearchTree
    bin_tree = BinarySearchTree()
    return MyBSTFix(bin_tree, request.param, None, None)


def test_bst_init_node(empty_bst):
    from bst import Node
    a = Node(empty_bst.input_val)
    assert empty_bst.input_val == a.val


def test_bst_init_node_has_left(empty_bst):
    from bst import Node
    a = Node(empty_bst.input_val,
             empty_bst.input_val,
             empty_bst.input_val,
             empty_bst.input_val
             )
    assert a.has_left_child() == empty_bst.input_val


def test_bst_init_node_has_right(empty_bst):
    from bst import Node
    a = Node(empty_bst.input_val,
             empty_bst.input_val,
             empty_bst.input_val,
             empty_bst.input_val
             )
    assert a.has_right_child() == empty_bst.input_val


def _test_bst_init_empty_tree(empty_bst):
    assert empty_bst.bin_tree.root is None


def test_bst_init_bin_tree():
    from bst import BinarySearchTree
    a = BinarySearchTree(1)
    assert a.root.val == 1


def test_bst_insert(empty_bst):
    empty_bst.bin_tree.insert(empty_bst.input_val)
    assert empty_bst.bin_tree.root.val == empty_bst.input_val


def test_bst_insert_with_existing_node_right(empty_bst):
    empty_bst.bin_tree.insert(empty_bst.input_val)
    empty_bst.bin_tree.insert(empty_bst.input_val * 2)
    assert empty_bst.bin_tree.root.right


def test_bst_insert_with_existing_node(empty_bst):
    empty_bst.bin_tree.insert(empty_bst.input_val * 2)
    empty_bst.bin_tree.insert(empty_bst.input_val)
    assert empty_bst.bin_tree.root.left


def test_find_node_with_one_node_in_tree(empty_bst):
    empty_bst.bin_tree.insert(empty_bst.input_val)
    result = empty_bst.bin_tree.find_node(empty_bst.input_val)
    assert result.val == empty_bst.input_val


def test_find_node_with_two_node_in_tree(empty_bst):
    empty_bst.bin_tree.insert(empty_bst.input_val)
    empty_bst.bin_tree.insert(empty_bst.input_val * 2)
    result = empty_bst.bin_tree.find_node(empty_bst.input_val * 2)
    assert result.val == empty_bst.input_val * 2


def test_find_node_with_three_node_in_tree(empty_bst):
    empty_bst.bin_tree.insert(empty_bst.input_val * 10)
    empty_bst.bin_tree.insert(empty_bst.input_val)
    empty_bst.bin_tree.insert(empty_bst.input_val * 5)
    result = empty_bst.bin_tree.find_node(empty_bst.input_val)
    assert result.val == empty_bst.input_val


def test_left_setter():
    from bst import Node
    node1 = Node(9)
    node2 = Node(7)
    node1.left = node2
    assert node1.left.val == node2.val
