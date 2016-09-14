# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bst import BST


def test_insert_from_empty():
    """Test insert into empty binary search tree."""
    bst = BST()
    bst.insert(1)
    assert bst.root.val == 1


def test_iterable_passed_to_BST():
    """Test iterable can be passed to initialize BST."""
    bst = BST([1, 2, 3])
    assert bst.contains(1) is True


def test_insert_correct_place_start_empty():
    """Test insert into correct place from empty bst."""
    bst = BST()
    bst.insert(1)
    bst.insert(2)
    assert bst.root.right.val == 2


def test_insert_from_existing(bst_test_case):
    """Test insert into correct position bst with existing values."""
    bst_test_case.insert(3)
    assert bst_test_case.root.left.left.val == 3


def test_insert_ignore_existing(bst_test_case):
    """Test insert existing value is ignored."""
    bst_test_case.insert(10)
    assert bst_test_case.size() == 5


def test_contains_true(bst_test_case):
    """Test contains returns true if value is in tree."""
    assert bst_test_case.contains(25)


def test_contains_true_root_is_value(bst_test_case):
    """Test true returned when root is the value searched."""
    assert bst_test_case.contains(10)


def test_contains_true_left_side_tree(bst_test_case):
    """Test true returned when val is found on left side of BST."""
    assert bst_test_case.contains(4)


def test_contains_false(bst_test_case):
    """Test contains returns false if value is not in tree."""
    assert bst_test_case.contains(13) is False


def test_contains_empty():
    """Test contains returns false if passed an empty bst."""
    bst = BST()
    assert bst.contains(1) is False


def test_size(bst_test_case):
    """Test size."""
    assert bst_test_case.size() == 5


def test_size_empty():
    """Test size returns 0 if passed an empty bst."""
    bst = BST()
    assert bst.size() == 0


def test_depth_empty():
    """Test depth empty."""
    bst = BST()
    assert bst.depth() == 0


def test_depth_existing_bst(bst_test_case):
    assert bst_test_case.depth() == 3


def test_depth_changes_after_insert(bst_test_case):
    starting_depth = bst_test_case.depth()
    bst_test_case.insert(88)
    new_depth = bst_test_case.depth()
    assert starting_depth < new_depth


def test_balance_empty_bst():
    bst = BST()
    assert bst.balance() == 0 


def test_balance_root_only():
    bst = BST()
    bst.insert(5)
    assert bst.balance() == 0 


def test_balance_balanced(bst_test_case):
    assert bst_test_case.balance() == 0


def test_balance_left_heavy(bst_test_case):
    bst_test_case.insert(1)
    bst_test_case.insert(3)
    assert bst_test_case.balance() == 1


def test_balance_left_super_heavy():
    bst = BST()
    bst.insert(100)
    bst.insert(90)
    bst.insert(88)
    bst.insert(70)
    assert bst.balance() == 3


def test_balance_right_heavy(bst_test_case):
    bst_test_case.insert(38)
    assert bst_test_case.balance() == -1


def test_balance_right_super_heavy(bst_test_case):
    bst_test_case.insert(38)
    bst_test_case.insert(40)
    bst_test_case.insert(50)
    bst_test_case.insert(132)
    bst_test_case.insert(200)
    bst_test_case.insert(1000)
    assert bst_test_case.balance() == -6
