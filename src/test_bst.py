# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bst import BST
import pytest


def test_insert_from_empty():
    '''Test insert into empty binary search tree.'''
    bst = BST()
    bst.insert(1)
    assert bst.root.val == 1


def test_iterable_passed_to_bst():
    '''Test iterable can be passed to initialize BST.'''
    bst = BST([1, 2, 3])
    assert bst.contains(1) is True


def test_insert_correct_place_start_empty():
    '''Test insert into correct place from empty bst.'''
    bst = BST()
    bst.insert(1)
    bst.insert(2)
    assert bst.root.right.val == 2


def test_insert_from_existing(bst_test_case):
    '''Test insert into correct position bst with existing values.'''
    bst_test_case.insert(3)
    assert bst_test_case.root.left.left.val == 3


def test_insert_ignore_existing(bst_test_case):
    '''Test insert existing value is ignored.'''
    bst_test_case.insert(10)
    assert bst_test_case.size() == 5


def test_contains_true(bst_test_case):
    '''Test contains returns true if value is in tree.'''
    assert bst_test_case.contains(25)


def test_contains_true_root_is_value(bst_test_case):
    '''Test true returned when root is the value searched.'''
    assert bst_test_case.contains(10)


def test_contains_true_left_side_tree(bst_test_case):
    '''Test true returned when val is found on left side of BST.'''
    assert bst_test_case.contains(4)


def test_contains_false(bst_test_case):
    '''Test contains returns false if value is not in tree.'''
    assert bst_test_case.contains(13) is False


def test_contains_empty():
    '''Test contains returns false if passed an empty bst.'''
    bst = BST()
    assert bst.contains(1) is False


def test_size(bst_test_case):
    '''Test size.'''
    assert bst_test_case.size() == 5


def test_size_empty():
    '''Test size returns 0 if passed an empty bst.'''
    bst = BST()
    assert bst.size() == 0


def test_depth_empty():
    '''Test depth empty.'''
    bst = BST()
    assert bst.depth() == 0


def test_depth_existing_bst(bst_test_case):
    '''Test depth existing bst.'''
    assert bst_test_case.depth() == 3


def test_depth_changes_after_insert(bst_test_case):
    '''Test depth changes bst after insert.'''
    starting_depth = bst_test_case.depth()
    bst_test_case.insert(88)
    new_depth = bst_test_case.depth()
    assert starting_depth < new_depth


def test_balance_empty_bst():
    '''Test balance is 0 if bst is empty.'''
    bst = BST()
    assert bst.balance() == 0


def test_balance_root_only():
    '''Test balance is 0 if bst only has root.'''
    bst = BST()
    bst.insert(5)
    assert bst.balance() == 0


def test_balance_balanced(bst_test_case):
    '''Test balance is 0 if left and right depths are equal.'''
    assert bst_test_case.balance() == 0


def test_balance_left_heavy(bst_test_case):
    '''Test balance is positive if left is greater than right depth.'''
    bst_test_case.insert(1)
    bst_test_case.insert(3)
    assert bst_test_case.balance() == 1


def test_balance_left_super_heavy():
    '''Test balance is positive if left is much greater than right depth.'''
    bst = BST()
    bst.insert(100)
    bst.insert(90)
    bst.insert(88)
    bst.insert(70)
    assert bst.balance() == 3


def test_balance_right_heavy(bst_test_case):
    '''Test balance is negative if right is greater than left depth.'''
    bst_test_case.insert(38)
    assert bst_test_case.balance() == -1


def test_balance_right_super_heavy(bst_test_case):
    '''Test balance is negative if right is much greater than left depth.'''
    bst_test_case.insert(38)
    bst_test_case.insert(40)
    bst_test_case.insert(50)
    bst_test_case.insert(132)
    bst_test_case.insert(200)
    bst_test_case.insert(1000)
    assert bst_test_case.balance() == -6


def test_in_order_traversal_empty_bst():
    '''Test appropreat error when in order is called on nothing.'''
    bst = BST()
    with pytest.raises(StopIteration) as message:
        next(bst.in_order())
    assert "Nothing to traverse." in str(message)


def test_in_order_traversal(bst_test_case):
    '''Test generator returns values in in-order traversal.'''
    assert next(bst_test_case.in_order()) is not None


def test_in_order_traversal_first_val(bst_test_case):
    '''Test generator returns correct fist value in in-order traversal.'''
    bst_test_case.insert(3)
    assert next(bst_test_case.in_order()) == 3


def test_in_order_traversal_second_val(bst_test_case):
    '''Test generator returns correct second value in in-order traversal.'''
    gen = bst_test_case.in_order()
    next(gen)
    assert next(gen) == 9


def test_in_order_traversal_eigth_val(bst_test_case_two):
    '''Test generator returns correct eighth value in in-order traversal.'''
    gen = bst_test_case_two.in_order()
    for _ in range(7):
        next(gen)
    assert next(gen) == 25


def test_in_order_traversal_last_val(bst_test_case_two):
    '''Test generator returns correct last value in in-order traversal.'''
    gen = bst_test_case_two.in_order()
    for _ in range(12):
        next(gen)
    assert next(gen) == 48


def test_in_order_traversal_penaltimate_val(bst_test_case_two):
    '''Test generator returns correct penultimate value in in-order traversal.'''
    gen = bst_test_case_two.in_order()
    for _ in range(11):
        next(gen)
    assert next(gen) == 37


def test_in_order_traversal_complete_traversal(bst_test_case):
    '''Test generator returns appropreate error when next more than nodes.'''
    gen = bst_test_case.in_order()
    for _ in range(5):
        next(gen)
    with pytest.raises(StopIteration):
        next(gen)


def test_pre_order_empty():
    '''Test appropreat error when pre order is called on nothing.'''
    bst = BST()
    with pytest.raises(StopIteration) as message:
        next(bst.pre_order())
    assert "Nothing to traverse." in str(message)


def test_pre_order_traversal(bst_test_case):
    '''Test generator returns values in pre-order traversal.'''
    assert next(bst_test_case.in_order()) is not None


def test_pre_order_traversal_first_val(bst_test_case):
    '''Test generator returns correct fist value in pre order traversal.'''
    assert next(bst_test_case.pre_order()) == 10


def test_pre_order_traversal_second_val(bst_test_case):
    '''Test generator returns correct second value pre order traversal.'''
    gen = bst_test_case.pre_order()
    next(gen)
    assert next(gen) == 4


def test_pre_order_traversal_eigth_val(bst_test_case_two):
    '''Test generator returns correct 8th value in pre order traversal.'''
    gen = bst_test_case_two.pre_order()
    for _ in range(7):
        next(gen)
    assert next(gen) == 22


def test_pre_order_traversal_last_val(bst_test_case_two):
    '''Test generator returns correct last value for pre order traversal.'''
    gen = bst_test_case_two.pre_order()
    for _ in range(12):
        next(gen)
    assert next(gen) == 48


def test_pre_order_traversal_penaltimate_val(bst_test_case_two):
    '''Test generator returns correct penultimate value for pre order traversal.'''
    gen = bst_test_case_two.pre_order()
    for _ in range(11):
        next(gen)
    assert next(gen) == 34


def test_pre_order_traversal_complete_traversal(bst_test_case):
    '''Test generator returns appropreate error when next more than nodes.'''
    gen = bst_test_case.pre_order()
    for _ in range(5):
        next(gen)
    with pytest.raises(StopIteration):
        next(gen)






def test_post_order_empty():
    '''Test appropostat error when post order is called on nothing.'''
    bst = BST()
    with pytest.raises(StopIteration) as message:
        next(bst.post_order())
    assert "Nothing to traverse." in str(message)


def test_post_order_traversal(bst_test_case):
    '''Test generator returns values in post-order traversal.'''
    assert next(bst_test_case.post_order()) is not None


def test_post_order_traversal_first_val(bst_test_case_two):
    '''Test generator returns correct fist value in post order traversal.'''
    assert next(bst_test_case_two.post_order()) == 1


def test_post_order_traversal_second_val(bst_test_case_two):
    '''Test generator returns correct second value post order traversal.'''
    gen = bst_test_case_two.post_order()
    next(gen)
    assert next(gen) == 3


def test_post_order_traversal_eigth_val(bst_test_case_two):
    '''Test generator returns correct 8th value in post order traversal.'''
    gen = bst_test_case_two.post_order()
    for _ in range(7):
        next(gen)
    assert next(gen) == 33


def test_post_order_traversal_last_val(bst_test_case_two):
    '''Test generator returns correct last value for post order traversal.'''
    gen = bst_test_case_two.post_order()
    for _ in range(12):
        next(gen)
    assert next(gen) == 10


def test_post_order_traversal_penaltimate_val(bst_test_case_two):
    '''Test generator returns correct penultimate value for post order traversal.'''
    gen = bst_test_case_two.post_order()
    for _ in range(11):
        next(gen)
    assert next(gen) == 25


def test_post_order_traversal_complete_traversal(bst_test_case):
    '''Test generator returns appropreate error when next more than nodes.'''
    gen = bst_test_case.pre_order()
    for _ in range(5):
        next(gen)
    with pytest.raises(StopIteration):
        next(gen)


def test_post_order():
    '''Test post order returns values in expected order.'''
    pass


def test_breadth_first():
    '''Do you even read our docstrings?'''
    pass
