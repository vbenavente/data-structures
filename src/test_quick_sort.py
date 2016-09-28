# -*- coding: utf-8 -*-
from quick_sort import quick_sort


def test_quick_sort():
    """Test merge sort sorts any list passed in."""
    result = quick_sort([5, 30, 20, 3, 17, 11, 2, 6, 35])
    assert result == sorted([5, 30, 20, 3, 17, 11, 2, 6, 35])
