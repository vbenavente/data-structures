# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bst import BST


def test_insert_from_empty():
    """Test insert into empty binary search tree."""
    bst = BST()
    bst.insert(1)
    assert bst.root.val == 1


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
