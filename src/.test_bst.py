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
    ('bin_tree', 'input_val', 'error_gen', 'length', 'sorted_list')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def full_bst(request):
    '''return an empty Simple Graph'''
    from bst import BinarySearchTree
    bin_tree = BinarySearchTree()
    length = len(request.param)
    sorted_list = sorted(request.param)
    for val in request.param:
        bin_tree.insert(val)
    if request.param or isinstance(request.param[0], int):
        input_val = 999
        error_gen = 'STRING!'
    else:
        input_val = 'STRING!!'
        error_gen - 999
    return MyBSTFix(bin_tree, input_val, error_gen, length, sorted_list)


@pytest.fixture(scope='function', params=[1, 5, 9, 15, 25, 'a', 'd', 'q'])
def empty_bst(request):
    '''return an empty Simple Graph'''
    from bst import BinarySearchTree
    bin_tree = BinarySearchTree()
    return MyBSTFix(bin_tree, request.param, None, None, None)


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


def test_left_setter_child():
    from bst import Node
    node1 = Node(9)
    node2 = Node(7)
    node1.left = node2
    assert node1.left.val == node2.val


def test_left_setter_parent():
    from bst import Node
    node1 = Node(9)
    node2 = Node(7)
    node1.left = node2
    assert node2.parent.val == node1.val


def test_right_setter_child():
    from bst import Node
    node1 = Node(7)
    node2 = Node(9)
    node1.right = node2
    assert node1.right.val == node2.val


def test_right_setter_parent():
    from bst import Node
    node1 = Node(7)
    node2 = Node(9)
    node1.right = node2
    assert node2.parent.val == node1.val


def test_del_left_child():
    from bst import Node
    node1 = Node(9)
    node2 = Node(7)
    node1.left = node2
    del node1.left
    assert node1.left is None


def test_del_left_child_error():
    from bst import Node
    node1 = Node(9)
    del node1.left
    assert node1.left is None


def test_del_right_child():
    from bst import Node
    node1 = Node(7)
    node2 = Node(9)
    node1.right = node2
    del node1.right
    assert node1.right is None


def test_del_right_child_error():
    from bst import Node
    node1 = Node(9)
    del node1.right
    assert node1.right is None


def test_parent_setter_child_parent():
    from bst import Node
    node1 = Node(1)
    node2 = Node(2)
    node2.parent = node1
    assert node1.val == node2.parent.val


def test_parent_setter_parent_child_right():
    from bst import Node
    node1 = Node(1)
    node2 = Node(2)
    node2.parent = node1
    assert node1.right.val == node2.val


def test_parent_setter_parent_child_left():
    from bst import Node
    node1 = Node(2)
    node2 = Node(1)
    node2.parent = node1
    assert node1.left.val == node2.val


def test_in_order_traversal(full_bst):
    results = full_bst.bin_tree.in_order()
    assert list(results) == full_bst.sorted_list


def test_in_order_traversal_empty_tree(empty_bst):
    with pytest.raises(IndexError):
        empty_bst.bin_tree.in_order()


def test_pre_order_traversal(empty_bst):
    results = [10, 5, 3, 7, 15, 13, 17]
    tree = empty_bst.bin_tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    tree.insert(17)
    assert list(tree.pre_order()) == results


def test_pre_order_traversal_empty_tree(empty_bst):
    with pytest.raises(IndexError):
        empty_bst.bin_tree.pre_order()


def test_post_order_traversal(empty_bst):
    results = [3, 7, 5, 13, 17, 15, 10]
    tree = empty_bst.bin_tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    tree.insert(17)
    assert list(tree.post_order()) == results


def test_post_order_traversal_empty_tree(empty_bst):
    with pytest.raises(IndexError):
        empty_bst.bin_tree.post_order()


def test_contains_true(full_bst):
    tree = full_bst.bin_tree
    result = tree.contains(full_bst.sorted_list[1])
    assert result


def test_contains_false(empty_bst):
    tree = empty_bst.bin_tree
    result = tree.contains(1000)
    assert not result


def test_depth(empty_bst):
    tree = empty_bst.bin_tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    tree.insert(17)
    result = tree.depth()
    assert result == 3


def test_empty_tree_depth(empty_bst):
    result = empty_bst.bin_tree.depth()
    assert result == 0


def test_balance_balanced(empty_bst):
    tree = empty_bst.bin_tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    tree.insert(17)
    result = tree.balance()
    assert result == 0


def test_balance_negative(empty_bst):
    tree = empty_bst.bin_tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(13)
    tree.insert(17)
    result = tree.balance()
    assert result == -1


def test_balance_positive(empty_bst):
    tree = empty_bst.bin_tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(15)
    result = tree.balance()
    assert result == 1


def test_breadth_first(empty_bst):
    tree = empty_bst.bin_tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    tree.insert(17)
    result = [10, 5, 15, 3, 7, 13, 17]
    assert list(tree.breadth_first()) == result


def test_breadth_first_empty_tree(empty_bst):
    tree = empty_bst.bin_tree
    with pytest.raises(IndexError):
        next(tree.breadth_first())
