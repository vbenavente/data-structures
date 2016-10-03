# -*- coding: utf-8 -*-

"""
Test file for the quicksort.py.

Tests the following functions: qs, qsh, part
"""

import pytest
import random
from quicksort import qs, qsh, part

INT_CASES = [random.sample(range(1000),
             random.randrange(2, 100)) for n in range(10)
             ]


def test_no_list_input():
    with pytest.raises(TypeError):
        qs('a')


def test_dict_input():
    with pytest.raises(TypeError):
        qs({})


def test_int_input():
    with pytest.raises(TypeError):
        qs(1)


def test_qsh_low_high():
    a = [1, 2, 3]
    b = qsh(a, 1, 0)
    assert a == b


def test_part():
    a = [1, 3, 2]
    b = part(a, 0, 2)
    assert b == 0
