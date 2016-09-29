# -*- coding: utf-8 -*-
from merge_sort import merge_sort


def test_merge_sort():
    """Test merge sort sorts any list passed in."""
    result = merge_sort([3, 8, 2, 82, 38])
    assert result == sorted([3, 8, 2, 82, 38])
