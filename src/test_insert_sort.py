# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import pytest

TEST_LIST = [
    (random.sample(range(100), random.randint(1, 50)))
]


@pytest.mark.parametrize('test_list', TEST_LIST)
def test_insertion_sort_random(test_list):
    from insert_sort import insert_sort
    assert insert_sort(test_list) == sorted(test_list)
