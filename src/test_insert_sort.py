# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import copy
import random
import pytest


TEST_LIST = [
    [], [8]
]

for x in range(0, 10):
    y = (random.sample(range(100), random.randint(1, 50)))
    TEST_LIST.append(y)


@pytest.mark.parametrize('test_list', TEST_LIST)
def test_insertion_sort_random(test_list):
    from insert_sort import insert_sort
    start_list = copy.copy(test_list)
    insert_sort(test_list)
    assert test_list == sorted(start_list)


def test_best_case():
    from insert_sort import BEST_CASE
    assert type(BEST_CASE) is list


def test_worst_case():
    from insert_sort import WORST_CASE
    assert type(WORST_CASE) is list
